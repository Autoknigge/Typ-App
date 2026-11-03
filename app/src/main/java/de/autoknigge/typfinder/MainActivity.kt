package de.autoknigge.typfinder

import android.graphics.Color
import android.graphics.Paint
import android.graphics.Typeface
import android.graphics.drawable.GradientDrawable
import android.os.Bundle
import android.view.Gravity
import android.view.View
import android.view.ViewGroup
import android.widget.FrameLayout
import android.widget.LinearLayout
import android.widget.ScrollView
import android.widget.TextView
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.WindowCompat
import org.json.JSONArray
import org.json.JSONObject

/** Enneagramm Typ-Finder: geführte Befragung zu Seite, Instinkt, Typ, Untertyp und Flügel. */
class MainActivity : AppCompatActivity() {

    companion object {
        private const val URL_APPS = "https://autoknigge.de/apps/"
        private const val URL_IMPRINT = "https://autoknigge.de/impressum"
        private const val URL_PRIVACY = "https://autoknigge.de/typfinder/datenschutz.html"
        private val GOLD = Color.parseColor("#D4AF37")
        private val INK = Color.parseColor("#F1EEDC")
        private val DIM = Color.parseColor("#B9C4BC")
        private val PANEL = Color.parseColor("#17301F")
        private val LINE = Color.parseColor("#2C4A38")
        private const val MATCH = ViewGroup.LayoutParams.MATCH_PARENT
        private const val WRAP = ViewGroup.LayoutParams.WRAP_CONTENT
    }

    private lateinit var prefs: android.content.SharedPreferences
    private lateinit var adManager: AdManager
    private lateinit var host: FrameLayout
    private val back = ArrayList<() -> Unit>()

    private fun dp(n: Int) = (n * resources.displayMetrics.density).toInt()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        WindowCompat.setDecorFitsSystemWindows(window, false)
        prefs = getSharedPreferences("typfinder", MODE_PRIVATE)

        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setBackgroundResource(R.drawable.bg_screen)
        }
        Ui.insets(root)
        host = FrameLayout(this)
        root.addView(host, LinearLayout.LayoutParams(MATCH, 0, 1f))
        val adSettings = link("Werbe-Einstellungen", null)
        val footer = LinearLayout(this).apply { gravity = Gravity.CENTER; setPadding(dp(4), 0, dp(4), 0) }
        footer.addView(link("Datenschutz", URL_PRIVACY))
        footer.addView(text("·", 12f, GOLD))
        footer.addView(link("Impressum", URL_IMPRINT))
        footer.addView(text("·", 12f, GOLD))
        footer.addView(adSettings)
        footer.addView(text("·", 12f, GOLD))
        footer.addView(link("Weitere Apps", URL_APPS))
        root.addView(footer, LinearLayout.LayoutParams(MATCH, WRAP))
        val adBox = FrameLayout(this).apply {
            setBackgroundResource(R.drawable.bg_ad)
            minimumHeight = dp(60)
        }
        root.addView(adBox, LinearLayout.LayoutParams(MATCH, WRAP))
        setContentView(root)
        adManager = AdManager(this, adBox, adSettings, true)

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (back.isEmpty()) { isEnabled = false; onBackPressedDispatcher.onBackPressed() } else back.removeAt(back.size - 1)()
            }
        })
        showHome()
        showIntro { adManager.start() }
    }

    // ------------------------------------------------------------------ Bausteine

    private fun text(t: String, size: Float, color: Int, bold: Boolean = false) = TextView(this).apply {
        text = t
        textSize = size
        setTextColor(color)
        if (bold) setTypeface(typeface, Typeface.BOLD)
    }

    private fun link(label: String, url: String?) = text(label, 12f, GOLD).apply {
        paintFlags = paintFlags or Paint.UNDERLINE_TEXT_FLAG
        setPadding(dp(6), dp(8), dp(6), dp(8))
        maxLines = 1
        if (url != null) setOnClickListener { Ui.openUrl(this@MainActivity, url) }
    }

    private fun card(bg: Int = PANEL, stroke: Int = LINE) = GradientDrawable().apply {
        setColor(bg)
        setStroke(dp(1), stroke)
        cornerRadius = dp(14).toFloat()
    }

    private fun lp(top: Int = 0) = LinearLayout.LayoutParams(MATCH, WRAP).apply { topMargin = dp(top) }

    private fun bigButton(icon: String, title: String, sub: String, onClick: () -> Unit): View = LinearLayout(this).apply {
        orientation = LinearLayout.HORIZONTAL
        gravity = Gravity.CENTER_VERTICAL
        background = card()
        setPadding(dp(14), dp(12), dp(14), dp(12))
        isClickable = true
        setOnClickListener { onClick() }
        addView(text(icon, 26f, INK), LinearLayout.LayoutParams(dp(46), WRAP))
        val col = LinearLayout(this@MainActivity).apply { orientation = LinearLayout.VERTICAL }
        col.addView(text(title, 17f, INK, true))
        if (sub.isNotEmpty()) col.addView(text(sub, 13f, DIM))
        addView(col, LinearLayout.LayoutParams(0, WRAP, 1f))
        addView(text("›", 24f, GOLD, true))
    }

    private fun push(prev: () -> Unit) { back.add(prev) }

    private fun screen(title: String, backTo: (() -> Unit)?, content: (LinearLayout) -> Unit): LinearLayout {
        host.removeAllViews()
        val root = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL }
        val top = LinearLayout(this).apply { gravity = Gravity.CENTER_VERTICAL; setPadding(dp(6), dp(4), dp(14), dp(4)) }
        if (backTo != null) {
            top.addView(text("‹", 32f, GOLD).apply {
                gravity = Gravity.CENTER
                contentDescription = "Zurück"
                setOnClickListener { backTo() }
            }, LinearLayout.LayoutParams(dp(46), dp(46)))
        } else top.setPadding(dp(16), dp(10), dp(14), dp(4))
        if (title.isNotEmpty()) {
            top.addView(text(title, 20f, GOLD, true).apply { maxLines = 1 })
            root.addView(top, LinearLayout.LayoutParams(MATCH, WRAP))
        }
        val col = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL; setPadding(dp(14), dp(6), dp(14), dp(14)) }
        content(col)
        root.addView(ScrollView(this).apply { addView(col, ViewGroup.LayoutParams(MATCH, WRAP)) }, LinearLayout.LayoutParams(MATCH, 0, 1f))
        host.addView(root, FrameLayout.LayoutParams(MATCH, MATCH))
        return root
    }

    // ------------------------------------------------------------------ Werbehinweis

    private fun showIntro(then: () -> Unit) {
        if (prefs.getBoolean("intro_seen", false)) { then(); return }
        AlertDialog.Builder(this)
            .setTitle("Kostenlos dank Werbung")
            .setMessage(
                "Diese App ist kostenlos und finanziert sich durch Werbung: ein Banner am unteren Rand und gelegentlich eine Anzeige.\n\n" +
                    "Im nächsten Schritt kannst du der Nutzung deiner Daten für Werbezwecke zustimmen und damit die kostenlose App unterstützen. " +
                    "Deine Auswahl kannst du jederzeit unter „Werbe-Einstellungen“ ändern."
            )
            .setCancelable(false)
            .setPositiveButton("Weiter") { _, _ ->
                prefs.edit().putBoolean("intro_seen", true).apply()
                then()
            }
            .show()
    }

    // ------------------------------------------------------------------ Start

    private fun showHome() {
        back.clear()
        screen("", null) { c ->
            val ver = try { packageManager.getPackageInfo(packageName, 0).versionName ?: "" } catch (e: Exception) { "" }
            val logoBox = FrameLayout(this)
            logoBox.addView(android.widget.ImageView(this).apply {
                setImageResource(R.drawable.logo_typfinder)
                adjustViewBounds = true
                contentDescription = "Enneagramm Typ-Finder"
            }, FrameLayout.LayoutParams(MATCH, WRAP))
            if (ver.isNotEmpty()) c.addView(text("v$ver", 11f, DIM).apply { gravity = Gravity.END }, LinearLayout.LayoutParams(MATCH, WRAP))
            c.addView(logoBox, LinearLayout.LayoutParams(MATCH, WRAP))
            val n = prefs.getString("tf_ans", "")!!.split(";").count { it.contains(":") }
            if (n > 0) c.addView(bigButton("▶️", "Fortsetzen", "$n Antworten gespeichert") { push { showHome() }; tfLoad(); showTypFinder() }, lp(20))
            c.addView(bigButton("🧭", if (n > 0) "Neu beginnen" else "Starten", "Etwa 10 bis 15 Minuten") {
                push { showHome() }; editIdx = -1; tfAnswers.clear(); tfSave(); showTypFinder()
            }, lp(if (n > 0) 10 else 20))
            val saved = savedList().length()
            if (saved > 0) c.addView(bigButton("💾", "Gespeicherte Ergebnisse", "$saved gespeichert") { push { showHome() }; showSavedList() }, lp(10))
        }
    }

    // ------------------------------------------------------------------ Typ-Finder

    private var tf: TypFinder? = null
    private val tfAnswers = LinkedHashMap<String, List<Int>>()

    private fun finder(): TypFinder {
        tf?.let { return it }
        val f = TypFinder(assets.open("typfinder.json").bufferedReader().use { it.readText() })
        tf = f
        return f
    }

    private fun tfLoad() {
        tfAnswers.clear()
        for (part in (prefs.getString("tf_ans", "") ?: "").split(";")) {
            val kv = part.split(":")
            if (kv.size == 2) {
                val sel = kv[1].split(",").mapNotNull { it.toIntOrNull() }
                if (sel.isNotEmpty()) tfAnswers[kv[0]] = sel
            }
        }
    }

    private fun tfSave() {
        prefs.edit().putString("tf_ans", tfAnswers.entries.joinToString(";") { "${it.key}:${it.value.joinToString(",")}" }).apply()
    }


    // ------------------------------------------------------------------ Zeitstrahl und Zwischenstand

    private val STAGES = listOf("Seite", "Instinkt", "Zentrum", "Blick", "Körper", "Typ", "Gegenprobe", "Untertyp", "Flügel")

    /** Zeitstrahl: wie weit der Ablauf schon ist (Schritte können je nach Antworten entfallen). */
    private fun timeline(stage: String?): View {
        val idx = if (stage == null) STAGES.size else STAGES.indexOf(stage).coerceAtLeast(0)
        val box = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL }
        val bars = LinearLayout(this).apply { orientation = LinearLayout.HORIZONTAL }
        for (i in STAGES.indices) {
            val col = when { i < idx -> GOLD; i == idx -> Color.parseColor("#F3DE8A"); else -> Color.parseColor("#34503F") }
            bars.addView(View(this).apply { setBackgroundColor(col) }, LinearLayout.LayoutParams(0, dp(6), 1f).apply { if (i > 0) leftMargin = dp(3) })
        }
        box.addView(bars, LinearLayout.LayoutParams(MATCH, WRAP))
        val label = if (stage == null) "Geschafft: Dein Ergebnis" else "Schritt ${idx + 1} von ${STAGES.size} · ${STAGES[idx]}"
        box.addView(text(label, 12f, DIM), lp(4))
        return box
    }

    /** Zwischenstand: drei Instinkt- und neun Typ-Knöpfe, Höhe des Balkens zeigt die derzeitige Tendenz. */
    private fun standPanel(typ: DoubleArray, inst: DoubleArray, finalResult: Boolean = false): View {
        val box = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL; background = card(); setPadding(dp(10), dp(8), dp(10), dp(10)) }
        fun norm(v: DoubleArray): DoubleArray {
            val mn = v.min(); val mx = v.max()
            return DoubleArray(v.size) { if (mx - mn < 0.5) 0.0 else (v[it] - mn) / (mx - mn) }
        }
        fun chips(labels: List<String>, vals: DoubleArray, names: List<String>, heightDp: Int): LinearLayout {
            val n = norm(vals); val best = if (vals.max() - vals.min() < 0.5) -1 else vals.indices.maxByOrNull { vals[it] } ?: -1
            val row = LinearLayout(this).apply { orientation = LinearLayout.HORIZONTAL }
            for (i in labels.indices) {
                val chip = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL; gravity = Gravity.CENTER_HORIZONTAL; isClickable = true }
                val track = FrameLayout(this).apply { setBackgroundColor(Color.parseColor("#22372B")) }
                val h = (dp(heightDp) * n[i]).toInt().coerceAtLeast(if (n[i] > 0) dp(3) else 0)
                track.addView(View(this).apply { setBackgroundColor(if (i == best) GOLD else Color.parseColor("#7C8F6A")) },
                    FrameLayout.LayoutParams(MATCH, h, Gravity.BOTTOM))
                chip.addView(track, LinearLayout.LayoutParams(MATCH, dp(heightDp)))
                chip.addView(text(labels[i], 14f, if (i == best) GOLD else INK, i == best).apply { gravity = Gravity.CENTER }, LinearLayout.LayoutParams(MATCH, WRAP).apply { topMargin = dp(3) })
                chip.setOnClickListener {
                    val stand = if (i == best) "derzeit am wahrscheinlichsten" else if (n[i] >= 0.6) "im Rennen" else "bisher eher unwahrscheinlich"
                    android.widget.Toast.makeText(this, "${names[i]}: $stand", android.widget.Toast.LENGTH_SHORT).show()
                }
                row.addView(chip, LinearLayout.LayoutParams(0, WRAP, 1f).apply { if (i > 0) leftMargin = dp(4) })
            }
            return row
        }
        box.addView(text(if (finalResult) "So liegt dein Ergebnis" else "Zwischenstand (wird mit jeder Antwort genauer)", 12f, DIM))
        box.addView(chips(listOf("sp", "so", "sx"), inst, listOf("Selbsterhaltender Untertyp (sp)", "Sozialer Untertyp (so)", "Sexuell / Beziehungsorientierter Untertyp (sx, 1:1)"), 13), lp(6))
        box.addView(chips((1..9).map { it.toString() }, typ.copyOfRange(1, 10), (1..9).map { "Typ $it · ${TypFinder.TYPE_NAMES[it]}" }, 20), lp(10))
        return box
    }

    private fun showTypFinder() {
        val step = finder().replay(tfAnswers)
        val res = step.result
        if (res != null) showTfResult(res, step.typeScores.copyOf(), step.instScores.copyOf()) else showTfRound(step)
    }

    private fun tfBack(step: TypFinder.Step) {
        if (step.lastRound.isEmpty()) { showHome(); return }
        for (id in step.lastRound) tfAnswers.remove(id)
        tfSave()
        showTypFinder()
    }


    /** Fragenkarten mit Mehrfachauswahl. sel enthält die schon gewählten Antworten und wird bei jedem Tippen aktualisiert. */
    private fun addQuestionCards(c: LinearLayout, qs: List<TFQuestion>, sel: HashMap<String, MutableSet<Int>>) {
        for (q in qs) {
            c.addView(text(q.q, 16f, INK, true), lp(18))
            val views = ArrayList<Pair<Int, TextView>>()
            fun restyle() {
                for ((idx, v) in views) {
                    val on = sel[q.id]?.contains(idx) == true
                    v.background = if (on) card(Color.parseColor("#3C3A1F"), GOLD) else card()
                }
            }
            val order = (q.o.indices).toList().shuffled(java.util.Random(q.id.hashCode().toLong()))
            for (idx in order + listOf(-1)) {
                val label = if (idx < 0) "Kann ich nicht genau sagen / keine passt wirklich" else q.o[idx].text
                val v = text(label, if (idx < 0) 13f else 15f, if (idx < 0) DIM else INK).apply {
                    setPadding(dp(14), dp(11), dp(14), dp(11))
                    isClickable = true
                    setOnClickListener {
                        val set = sel.getOrPut(q.id) { mutableSetOf() }
                        if (idx < 0) { set.clear(); set.add(-1) }
                        else if (q.o[idx].excl) { val was = set.contains(idx); set.clear(); if (!was) set.add(idx) }   // „Keine davon“ schließt die anderen Antworten aus
                        else { set.remove(-1); set.removeAll { it >= 0 && q.o[it].excl }; if (!set.add(idx)) set.remove(idx) }
                        if (set.isEmpty()) sel.remove(q.id)
                        restyle()
                    }
                }
                views.add(idx to v)
                c.addView(v, lp(8))
            }
            restyle()
        }
    }

    private fun showTfRound(step: TypFinder.Step) {
        val round = step.round ?: return
        back.clear(); push { tfBack(step) }
        val sel = HashMap<String, MutableSet<Int>>()
        screen("Typ-Finder", { tfBack(step) }, { c ->
            c.addView(timeline(round.name), lp(2))
            c.addView(standPanel(step.typeScores.copyOf(), step.instScores.copyOf()), lp(10))
            c.addView(text("Runde ${step.roundNo} · ${round.name}", 13f, GOLD, true), lp(14))
            c.addView(text("Wähle, was am ehesten zutrifft. Wenn du schwankst, darfst du mehrere Antworten antippen.", 12f, DIM), lp(2))
            if (round.name == "Seite") c.addView(text("Die Seite hat nichts mit dem Geschlecht zu tun. Frauen können einen männlichen, Männer einen weiblichen Gesamtausdruck haben. Wenn du es nicht genau sagen kannst, wähle „Kann ich nicht genau sagen“. Alle Angaben sind nur Hinweise und schließen nichts aus.", 12f, GOLD), lp(8))
            addQuestionCards(c, round.qs, sel)
            c.addView(bigButton("➡️", "Weiter", "") {
                if (round.qs.all { sel.containsKey(it.id) }) {
                    for ((id, set) in sel) tfAnswers[id] = set.sorted(); tfSave(); showTypFinder()
                } else android.widget.Toast.makeText(this, "Bitte jede Frage beantworten, oder „Kann ich nicht genau sagen“ wählen.", android.widget.Toast.LENGTH_SHORT).show()
            }, lp(22))
        })
    }

    private fun showTfResult(r: TFResult, finalType: DoubleArray, finalInst: DoubleArray, savedIdx: Int = -1) {
        val leave: () -> Unit = if (savedIdx >= 0) { { showSavedList() } } else { { showHome() } }
        back.clear(); push(leave)
        if (savedIdx < 0) adManager.showInterstitialIfDue()
        val top = r.types[0].first
        val sub = TypFinder.SUB[r.sub]
        val shareText = StringBuilder()
        screen("Deine Einschätzung", leave, { c ->
            c.addView(timeline(null), lp(2))
            c.addView(standPanel(finalType, finalInst, true), lp(10))
            val head = "Typ $top · ${TypFinder.TYPE_NAMES[top]}"
            c.addView(text(head, 20f, GOLD, true), lp(4))
            c.addView(text("Sicherheit: ${r.confidence}", 14f, INK), lp(2))
            if (r.confidence == "offen") c.addView(text("Zwei bis drei Typen liegen nah beieinander. Starte den Test später noch einmal oder beobachte dich im Alltag.", 13f, DIM), lp(4))
            c.addView(text("Seite", 13f, GOLD, true), lp(16))
            c.addView(text(when (top) { in 5..8 -> "Männliche Seite (5 bis 8): ausrichtende Kraft, „Ich setze in Bewegung.“"; in 1..4 -> "Weibliche Seite (1 bis 4): aufnehmende Kraft, „Ich lasse entstehen.“"; else -> "Die 9 vermittelt zwischen den beiden Seiten." }, 15f, INK), lp(2))
            c.addView(text("Instinkt", 13f, GOLD, true), lp(16))
            val i0 = TypFinder.INST_NAMES[r.inst[0].first] ?: ""
            c.addView(text(i0 + if (r.instOpen) "\nDer zweite Instinkt liegt nah dran: ${TypFinder.INST_NAMES[r.inst[1].first]}." else "", 15f, INK), lp(2))
            c.addView(text("Untertyp", 13f, GOLD, true), lp(14))
            if (sub != null) {
                c.addView(text("${r.sub} · ${sub.first}", 16f, INK, true), lp(2))
                c.addView(text(sub.second, 14f, DIM), lp(2))
                Dynamik.SUB[r.sub]?.let { dy ->
                    c.addView(text("Grundkonflikt von Typ $top", 13f, GOLD, true), lp(12))
                    c.addView(text(Dynamik.GRUNDKONFLIKT[top] ?: "", 14f, INK), lp(2))
                    c.addView(text("Unbewusste Dynamik · ${dy.name}", 13f, GOLD, true), lp(10))
                    c.addView(text(dy.dynamik, 14f, INK), lp(2))
                    c.addView(text("Entwicklung", 13f, GOLD, true), lp(10))
                    c.addView(text(dy.entwicklung, 14f, INK), lp(2))
                }
                c.addView(text("Art: ${TypFinder.subKind(r.sub)}", 13f, GOLD), lp(6))
                TypFinder.VERWECHSELT[r.sub]?.let { c.addView(text("Wird oft verwechselt mit: $it", 12f, DIM), lp(2)) }
                if (r.sub in TypFinder.KONTRA) c.addView(text("Hinweis: Kontratypen sind besonders schwer zu bestimmen, weil der Instinkt der Grundleidenschaft entgegenwirkt.", 12f, DIM), lp(6))
            }
            c.addView(text("Die Kernfrage", 13f, GOLD, true), lp(14))
            c.addView(text(Dynamik.KERNFRAGE, 14f, INK, true), lp(2))
            c.addView(text(Dynamik.HINWEIS, 12f, DIM), lp(4))
            c.addView(text("Flügel", 13f, GOLD, true), lp(14))
            c.addView(text(if (r.wing != null) "${top}w${r.wing}" else "Kein klarer Flügel erkennbar", 15f, INK), lp(2))
            if (r.pro.isNotEmpty()) {
                c.addView(text("Dafür sprach", 13f, GOLD, true), lp(14))
                for (s in r.pro) c.addView(text("• $s", 14f, INK), lp(4))
            }
            val run = r.types[1].first
            c.addView(text("Auch möglich: Typ $run · ${TypFinder.TYPE_NAMES[run]}", 13f, GOLD, true), lp(14))
            for (s in r.contra) c.addView(text("• $s", 14f, DIM), lp(4))
            if (top == 9 || run == 9) c.addView(text("Zur 9: Sie ist nicht einfach Passivität oder Konfliktvermeidung. Sieh sie erst dann als sichere Einordnung, wenn sich ein wiederkehrendes Muster des Vermittelns, Anpassens oder Verlusts des eigenen Standpunkts zeigt, nicht bloß, weil die Antworten gemischt ausgefallen sind.", 12f, DIM), lp(6))
            c.addView(text("Rangliste: " + r.types.joinToString(" · ") { "Typ ${it.first}" }, 13f, DIM), lp(10))
            c.addView(text("Grundlage: ${r.questionsAsked} Antworten. Das Ergebnis ist eine Einladung zum Prüfen, kein festes Etikett.", 12f, DIM), lp(8))
            c.addView(bigButton("📤", "Ergebnis teilen", "") {
                val msg = "Mein Ergebnis im Enneagramm Typ-Finder: Typ $top, ${r.sub}" + (r.wing?.let { ", Flügel ${top}w$it" } ?: "") + ". Sicherheit: ${r.confidence}. Eine Einladung zum Prüfen, kein Etikett."
                startActivity(android.content.Intent.createChooser(android.content.Intent(android.content.Intent.ACTION_SEND).apply { type = "text/plain"; putExtra(android.content.Intent.EXTRA_TEXT, msg) }, "Teilen"))
            }, lp(10))
            if (savedIdx < 0) {
                if (editIdx >= 0) c.addView(bigButton("💾", "Gespeichertes Ergebnis aktualisieren", "Mit den geänderten Antworten") { overwriteSaved(editIdx, r, finalType, finalInst) }, lp(10))
                c.addView(bigButton("💾", if (editIdx >= 0) "Als neues Ergebnis speichern" else "Ergebnis speichern", "Unter einem Namen auf diesem Handy") { askSaveName(r, finalType, finalInst) }, lp(10))
                c.addView(bigButton("🔄", "Neu beginnen", "") { editIdx = -1; tfAnswers.clear(); tfSave(); showTypFinder() }, lp(10))
            } else {
                val ans = savedList().getJSONObject(savedIdx).optString("ans", "")
                if (ans.isNotEmpty()) c.addView(bigButton("✏️", "Antworten ansehen und ändern", "Einzelne Kapitel noch einmal überdenken") {
                    editAns = decodeAns(ans); showEditChapters(savedIdx)
                }, lp(10))
                c.addView(bigButton("🗑️", "Dieses Ergebnis löschen", "") {
                    AlertDialog.Builder(this).setMessage("Dieses gespeicherte Ergebnis löschen?")
                        .setPositiveButton("Löschen") { _, _ -> deleteSaved(savedIdx); showSavedList() }
                        .setNegativeButton("Abbrechen", null).show()
                }, lp(10))
            }
            val code = r.sub + (r.wing?.let { "-${top}w$it" } ?: "")
            val hint = LinearLayout(this).apply {
                orientation = LinearLayout.VERTICAL
                background = card(Color.parseColor("#2A2A14"), GOLD)
                setPadding(dp(14), dp(12), dp(14), dp(14))
            }
            hint.addView(text("Genauer wissen?", 16f, GOLD, true))
            hint.addView(text("Die tiefgreifende, umfangreiche Analyse zu deinem Ergebnis bekommst du als PDF-Bericht ab 99 €: mit Erklärungen zu Typ, Untertyp und Flügel, Weiterentwicklung, Beruf und Beziehungen. Mehrere Analysen sind günstiger.", 13f, INK), lp(6))
            hint.addView(text("autoknigge.de/analyse", 14f, GOLD, true).apply { paintFlags = paintFlags or Paint.UNDERLINE_TEXT_FLAG }, lp(6))
            hint.addView(bigButton("🔎", "Mehr zur Analyse", "Öffnet autoknigge.de im Browser") { Ui.openUrl(this@MainActivity, "https://autoknigge.de/analyse?e=$code") }, lp(10))
            c.addView(hint, lp(22))
        })
    }



    // ------------------------------------------------------------------ Gespeicherte Ergebnisse (nur lokal)

    private fun savedList(): JSONArray = try { JSONArray(prefs.getString("tf_saved", "[]")) } catch (e: Exception) { JSONArray() }

    private fun writeSaved(arr: JSONArray) { prefs.edit().putString("tf_saved", arr.toString()).apply() }

    private fun deleteSaved(i: Int) {
        val old = savedList(); val n = JSONArray()
        for (k in 0 until old.length()) if (k != i) n.put(old.get(k))
        writeSaved(n)
    }

    private fun askSaveName(r: TFResult, ft: DoubleArray, fi: DoubleArray) {
        val fmt = java.text.SimpleDateFormat("dd.MM.yyyy", java.util.Locale.GERMANY)
        val et = android.widget.EditText(this).apply {
            setText("Ergebnis " + fmt.format(java.util.Date()))
            setSelectAllOnFocus(true)
            setSingleLine(true)
        }
        val box = FrameLayout(this).apply { setPadding(dp(20), dp(8), dp(20), 0); addView(et) }
        AlertDialog.Builder(this).setTitle("Name für das Ergebnis").setView(box)
            .setPositiveButton("Speichern") { _, _ ->
                val name = et.text.toString().trim().ifEmpty { "Ergebnis" }.take(60)
                val arr = JSONArray()
                arr.put(r.toJson().put("name", name).put("date", System.currentTimeMillis())
                    .put("ft", JSONArray(ft.toList())).put("fi", JSONArray(fi.toList())).put("ans", encodeAns(tfAnswers)))
                val old = savedList()
                for (k in 0 until old.length()) arr.put(old.get(k))
                writeSaved(arr)
                android.widget.Toast.makeText(this, "Gespeichert als „$name“", android.widget.Toast.LENGTH_SHORT).show()
            }
            .setNegativeButton("Abbrechen", null).show()
    }


    private fun encodeAns(m: Map<String, List<Int>>) = m.entries.joinToString(";") { "${it.key}:${it.value.joinToString(",")}" }

    private fun decodeAns(s: String): LinkedHashMap<String, List<Int>> {
        val out = LinkedHashMap<String, List<Int>>()
        for (part in s.split(";")) {
            val kv = part.split(":")
            if (kv.size == 2) { val sel = kv[1].split(",").mapNotNull { it.toIntOrNull() }; if (sel.isNotEmpty()) out[kv[0]] = sel }
        }
        return out
    }

    private val CHAPTERS = listOf("Seite", "Instinkt", "Zentrum", "Blick", "Körper", "Typ", "Untertyp", "Flügel")
    private fun chapterOf(st: String) = when (st) {
        "S" -> "Seite"; "A" -> "Instinkt"; "B" -> "Zentrum"; "K" -> "Blick"; "Z" -> "Körper"; "C" -> "Typ"; "D" -> "Untertyp"; else -> "Flügel"
    }

    private var editIdx = -1                                   // Nummer des gespeicherten Ergebnisses, das gerade überarbeitet wird
    private var editAns = LinkedHashMap<String, List<Int>>()   // Antworten während der Überarbeitung

    private fun openSaved(i: Int) {
        val arr = savedList()
        val o = arr.getJSONObject(i)
        val r = try { TFResult.fromJson(o) } catch (e: Exception) { return }
        val ft = o.optJSONArray("ft"); val fi = o.optJSONArray("fi")
        val ftd = DoubleArray(10) { j -> ft?.optDouble(j, 0.0) ?: 0.0 }
        val fid = DoubleArray(3) { j -> fi?.optDouble(j, 0.0) ?: 0.0 }
        showTfResult(r, ftd, fid, i)
    }

    /** Kapitelübersicht: einzelne Kapitel eines gespeicherten Ergebnisses noch einmal überdenken. */
    private fun showEditChapters(i: Int) {
        back.clear(); push { openSaved(i) }
        screen("Antworten ändern", { openSaved(i) }, { c ->
            c.addView(text("Tippe ein Kapitel an, um deine Antworten dort noch einmal zu überdenken und zu ändern. Danach wird das Ergebnis neu berechnet.", 13f, DIM), lp(4))
            for (ch in CHAPTERS) {
                val n = finder().bank.count { chapterOf(it.st) == ch && editAns.containsKey(it.id) }
                if (n == 0) continue
                c.addView(bigButton("✏️", ch, "$n Antworten") { showEditStage(i, ch) }, lp(10))
            }
            c.addView(bigButton("🔁", "Ergebnis neu berechnen", "Mit den geänderten Antworten") {
                tfAnswers.clear(); tfAnswers.putAll(editAns); tfSave(); editIdx = i; showTypFinder()
            }, lp(18))
        })
    }

    private fun showEditStage(i: Int, chapter: String) {
        back.clear(); push { showEditChapters(i) }
        val qs = finder().bank.filter { chapterOf(it.st) == chapter && editAns.containsKey(it.id) }
        val sel = HashMap<String, MutableSet<Int>>()
        for (q in qs) sel[q.id] = editAns.getValue(q.id).toMutableSet()
        screen(chapter, { showEditChapters(i) }, { c ->
            c.addView(text("Deine bisherigen Antworten sind markiert. Du kannst sie ändern.", 12f, DIM), lp(2))
            addQuestionCards(c, qs, sel)
            c.addView(bigButton("✔️", "Übernehmen", "") {
                for (q in qs) editAns[q.id] = (sel[q.id] ?: mutableSetOf(-1)).sorted()
                showEditChapters(i)
            }, lp(22))
        })
    }

    /** Neu berechnetes Ergebnis in den gespeicherten Eintrag übernehmen (Name bleibt). */
    private fun overwriteSaved(i: Int, r: TFResult, ft: DoubleArray, fi: DoubleArray) {
        val old = savedList()
        val keep = old.getJSONObject(i)
        val n = r.toJson().put("name", keep.optString("name", "Ergebnis")).put("date", System.currentTimeMillis())
            .put("ft", JSONArray(ft.toList())).put("fi", JSONArray(fi.toList())).put("ans", encodeAns(tfAnswers))
        old.put(i, n)
        writeSaved(old)
        editIdx = -1
        android.widget.Toast.makeText(this, "Gespeichertes Ergebnis aktualisiert", android.widget.Toast.LENGTH_SHORT).show()
    }

    private fun showSavedList() {
        back.clear(); push { showHome() }
        val arr = savedList()
        screen("Gespeicherte Ergebnisse", { showHome() }, { c ->
            if (arr.length() == 0) c.addView(text("Noch nichts gespeichert. Am Ende des Tests kannst du dein Ergebnis unter einem Namen speichern.", 14f, DIM), lp(8))
            val fmt = java.text.SimpleDateFormat("dd.MM.yyyy HH:mm", java.util.Locale.GERMANY)
            for (i in 0 until arr.length()) {
                val o = arr.getJSONObject(i)
                val r = try { TFResult.fromJson(o) } catch (e: Exception) { continue }
                val top = r.types[0].first
                val sub = "Typ $top · ${r.sub}" + (r.wing?.let { " · ${top}w$it" } ?: "") + " · ${r.confidence}"
                c.addView(bigButton("📋", o.optString("name", "Ergebnis"), fmt.format(java.util.Date(o.optLong("date"))) + "\n" + sub) { openSaved(i) }, lp(10))
            }
        })
    }

    override fun onPause() {
        if (::adManager.isInitialized) adManager.pause()
        super.onPause()
    }

    override fun onResume() {
        super.onResume()
        if (::adManager.isInitialized) adManager.resume()
    }

    override fun onDestroy() {
        if (::adManager.isInitialized) adManager.destroy()
        super.onDestroy()
    }
}
