package de.autoknigge.typfinder

/** Psychodynamische Grundkonflikte und Entwicklungsrichtungen der 27 Untertypen (Interpretation der Enneagramm-Tradition, insbesondere der Untertypenlehre nach Claudio Naranjo). */
object Dynamik {
    class Sub(val name: String, val dynamik: String, val entwicklung: String)

    val GRUNDKONFLIKT = mapOf(
        1 to "Zorn, Fehlerhaftigkeit und der Anspruch, richtig zu sein.",
        2 to "Eigene Bedürftigkeit, Liebe und Anerkennung.",
        3 to "Selbstwert, Identität und Anerkennung durch Leistung.",
        4 to "Mangel, Neid und die Suche nach der eigenen Identität.",
        5 to "Überforderung, Rückzug und das Bedürfnis nach Autonomie.",
        6 to "Angst, Unsicherheit und das Bedürfnis nach Orientierung.",
        7 to "Schmerzvermeidung, innere Leere und die Suche nach Möglichkeiten.",
        8 to "Verletzlichkeit, Kontrolle und die Angst vor Ausgeliefertsein.",
        9 to "Selbstvergessenheit, innere Trägheit und die Angst vor Trennung.")

    val SUB = mapOf(
        "SP1" to Sub("Angst", "Versucht, durch Vorsicht, Selbstkontrolle und Fehlervermeidung Sicherheit zu gewinnen.", "Unvollkommenheit zulassen."),
        "SO1" to Sub("Nichtanpassung", "Versucht, durch moralische Prinzipien und Vorbildlichkeit Orientierung zu schaffen.", "Andere Maßstäbe gelten lassen."),
        "SX1" to Sub("Eifer", "Versucht, durch Intensität, Leidenschaft und Verbesserungsdrang die Welt und Beziehungen in die richtige Richtung zu bewegen.", "Akzeptanz statt Korrektur."),
        "SP2" to Sub("Privileg", "Versucht, durch besondere Zuwendung und Unentbehrlichkeit bevorzugt und versorgt zu werden.", "Eigene Bedürfnisse offen aussprechen."),
        "SO2" to Sub("Ehrgeiz", "Versucht, durch Einfluss, Großzügigkeit und soziale Bedeutung einen besonderen Platz zu erhalten.", "Wert unabhängig von Bedeutung erfahren."),
        "SX2" to Sub("Verführung/Aggression", "Versucht, durch persönliche Anziehung, Intensität und Durchsetzung die gewünschte Nähe zu gewinnen.", "Liebe ohne Anspruch auf Erwiderung."),
        "SP3" to Sub("Sicherheit", "Versucht, durch Leistung, Zuverlässigkeit und Bescheidenheit Sicherheit zu schaffen, ohne sich in den Vordergrund zu stellen.", "Eigenen Wert unabhängig von Leistung erkennen."),
        "SO3" to Sub("Prestige", "Versucht, durch Erfolg, Status und gesellschaftliche Anerkennung seinen Wert zu bestätigen.", "Sein statt Scheinen."),
        "SX3" to Sub("Attraktivität", "Versucht, durch Ausstrahlung, Attraktivität und Anpassung an begehrte Ideale liebenswert und begehrenswert zu sein.", "Authentizität statt Inszenierung."),
        "SP4" to Sub("Zähigkeit", "Versucht, Mangel und Schmerz durch Ausdauer, Selbstbeherrschung und Durchhaltevermögen zu überwinden.", "Bedürfnisse und Verletzlichkeit zulassen."),
        "SO4" to Sub("Scham", "Versucht, durch Selbstvergleich und das Erleben eigener Unzulänglichkeit Zugehörigkeit und Anerkennung zu finden.", "Selbstannahme statt Selbstabwertung."),
        "SX4" to Sub("Konkurrenz", "Versucht, durch Intensität, Wettbewerb und Überlegenheit den eigenen Mangel zu überwinden.", "Selbstwert ohne Vergleich."),
        "SP5" to Sub("Rückzug/Burg", "Versucht, durch Abgrenzung, Unabhängigkeit und Begrenzung der eigenen Bedürfnisse Sicherheit zu gewinnen.", "Sich auf das Leben und andere einlassen."),
        "SO5" to Sub("Totem", "Versucht, durch Wissen, Ideale und Zugehörigkeit zu besonderen geistigen Gemeinschaften Bedeutung zu gewinnen.", "Wissen in lebendige Beziehungen übertragen."),
        "SX5" to Sub("Vertrauen", "Versucht, durch eine außergewöhnlich tiefe Zweierbindung Sicherheit und Vertrauen zu finden.", "Nähe zulassen, ohne sich ausschließlich auf eine Person zu stützen."),
        "SP6" to Sub("Wärme", "Versucht, durch Freundlichkeit, Verlässlichkeit und Schutzgemeinschaft Sicherheit zu finden.", "Eigenes Vertrauen stärken."),
        "SO6" to Sub("Pflicht", "Versucht, durch Regeln, Loyalität und Pflichterfüllung Unsicherheit zu kontrollieren.", "Eigenständiges Urteilen statt blindem Vertrauen in Autoritäten."),
        "SX6" to Sub("Stärke", "Versucht, durch Mut, Konfrontation und Stärke die eigene Angst zu überwinden.", "Verletzlichkeit zulassen, ohne Stärke zu verlieren."),
        "SP7" to Sub("Netzwerken/Familie", "Versucht, durch Kontakte, Gegenseitigkeit und geschickte Beziehungen Sicherheit und Versorgung zu gewährleisten.", "Nicht alles absichern und kontrollieren müssen."),
        "SO7" to Sub("Opferbereitschaft", "Versucht, durch Ideale, Großzügigkeit und Verzicht auf eigene Bedürfnisse moralische Zugehörigkeit zu gewinnen.", "Eigene Bedürfnisse und Grenzen anerkennen."),
        "SX7" to Sub("Suggestibilität", "Versucht, durch Begeisterung, Fantasie und idealisierte Möglichkeiten der Realität und ihren Begrenzungen zu entkommen.", "Wirklichkeit annehmen und Verbindlichkeit leben."),
        "SP8" to Sub("Befriedigung", "Versucht, durch Selbstversorgung, materielle Sicherheit und Unabhängigkeit niemandem etwas schuldig zu sein.", "Bedürfnisse und Abhängigkeit zulassen."),
        "SO8" to Sub("Solidarität/Mittäterschaft", "Versucht, durch Schutz, Loyalität und Führung eine starke Gemeinschaft zu schaffen.", "Nicht immer kämpfen oder bestimmen müssen."),
        "SX8" to Sub("Besitzergreifung", "Versucht, durch Intensität, Dominanz und Verschmelzung in Beziehungen absolute Nähe und Kontrolle zu gewinnen.", "Vertrauen ohne Besitzanspruch."),
        "SP9" to Sub("Appetit", "Versucht, durch Routinen, Komfort und vertraute Befriedigungen innere Ruhe und Sicherheit zu erhalten.", "Eigene Prioritäten aktiv verfolgen."),
        "SO9" to Sub("Teilhabe", "Versucht, durch Engagement und Aufgehen in der Gemeinschaft Zugehörigkeit und Bedeutung zu finden.", "Sich selbst innerhalb der Gruppe wahrnehmen."),
        "SX9" to Sub("Verschmelzung", "Versucht, durch Identifikation mit einer wichtigen Person Nähe und innere Einheit zu gewinnen.", "Eine eigenständige Identität und eigene Wünsche entwickeln."))

    /** Die drei Ebenen: Frage je Ebene. */
    val EBENEN = listOf(
        "Grundtyp" to "Welchen inneren Konflikt versuche ich unbewusst zu vermeiden?",
        "Untertyp" to "In welchem Lebensbereich versuche ich diesen Konflikt zu bewältigen?",
        "Entwicklung" to "Was müsste ich zulassen, was ich bisher unbewusst vermeide?")

    val EBENEN_TEXT = "Der Mensch entwickelt nicht einfach bestimmte Verhaltensweisen, sondern unbewusste Strategien, um einen inneren Mangel, eine Angst oder einen grundlegenden Konflikt nicht erleben zu müssen. Der Untertyp beschreibt, in welche Richtung diese Strategie gelenkt wird."
    val INSTINKT_RICHTUNG = listOf(
        "Selbsterhaltung (SP)" to "Sicherheit, Versorgung und Autonomie.",
        "Sozial (SO)" to "Zugehörigkeit, Bedeutung und Position in der Gemeinschaft.",
        "Sexualität/Anziehung (SX)" to "Intensität, Anziehung und besondere Verbindung.")
    val KERNFRAGE = "Was versuche ich durch mein Verhalten zu erreichen, und welches Gefühl versuche ich dadurch zu vermeiden?"
    val KERNFRAGE_TEXT = "Das eigentlich Spannende an der Selbsterkenntnis ist nicht, sich in einer Typenbeschreibung wiederzufinden, sondern genau das zu erkennen. Darin liegt der Unterschied zwischen einer oberflächlichen Typisierung und echter psychodynamischer Enneagramm-Arbeit."
    private val LEIDENSCHAFT = mapOf(1 to "Zorn", 2 to "Stolz", 3 to "Eitelkeit", 4 to "Neid", 5 to "Geiz", 6 to "Angst, Zweifel", 7 to "Völlerei", 8 to "Lust an Intensität", 9 to "Trägheit")

    /** Erklärt für den Untertyp [sub] (zum Beispiel „SX6“), was es bedeutet, Normaltyp, Verstärkungstyp oder Kontratyp zu sein. */
    fun artErklaerung(sub: String): String {
        val typ = sub.drop(2).toIntOrNull() ?: 0
        val leid = LEIDENSCHAFT[typ] ?: "Grundleidenschaft"
        val ins = when (sub.take(2)) {
            "SP" -> "Selbsterhaltung"
            "SO" -> "Sozial"
            else -> "Sexuell, Eins-zu-eins"
        }
        return when (TypFinder.subKind(sub)) {
            "Verstärkungstyp" -> "Was es bedeutet, ein Verstärkungstyp zu sein: Dein Instinkt ($ins) verstärkt die Grundleidenschaft deines Typs ($leid). Sie tritt bei dir besonders deutlich und kräftig hervor, und die Typbeschreibung passt oft sehr unmittelbar."
            "Kontratyp" -> "Was es bedeutet, ein Kontratyp zu sein: Dein Instinkt ($ins) wirkt der Grundleidenschaft deines Typs ($leid) entgegen. Die Grundmotivation bleibt dieselbe, wird aber unbewusst verneint oder versteckt. Deshalb passt dein Verhalten oft nicht zum erwarteten Typbild, und dein Typ ist schwerer zu erkennen."
            else -> "Was es bedeutet, ein Normaltyp zu sein: Dein Instinkt ($ins) und die Grundleidenschaft deines Typs ($leid) gehen in dieselbe Richtung. Sie zeigt sich bei dir in ihrer üblichen Form, und die Typbeschreibung passt meist unmittelbar."
        }
    }

    val HINWEIS = "Hinweis: Die Beschreibungen sind eine psychologische Interpretation der Enneagramm-Tradition, insbesondere der Untertypenlehre nach Claudio Naranjo."
}
