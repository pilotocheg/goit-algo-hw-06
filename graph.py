import networkx as nx

G = nx.Graph(
    name="Ukrainian cities",
)

G.add_nodes_from(
    [
        "Uzhorod",
        "Kyiv",
        "Lviv",
        "Poltava",
        "Chernihiv",
        "Sumy",
        "Kharkiv",
        "Dnipro",
        "Odesa",
        "Mykolaiv",
        "Zaporizhzhia",
        "Mariupol",
        "Vinnytsia",
    ]
)

G.add_edges_from(
    [
        ("Uzhorod", "Lviv", {"weight": 272}),
        ("Lviv", "Kyiv", {"weight": 545}),
        ("Kyiv", "Poltava", {"weight": 335}),
        ("Kyiv", "Chernihiv", {"weight": 147}),
        ("Chernihiv", "Sumy", {"weight": 160}),
        ("Poltava", "Sumy", {"weight": 99}),
        ("Kharkiv", "Poltava", {"weight": 144}),
        ("Kharkiv", "Dnipro", {"weight": 222}),
        ("Dnipro", "Zaporizhzhia", {"weight": 85}),
        ("Zaporizhzhia", "Mariupol", {"weight": 160}),
        ("Odesa", "Mykolaiv", {"weight": 134}),
        ("Kyiv", "Odesa", {"weight": 472}),
        ("Mykolaiv", "Zaporizhzhia", {"weight": 285}),
        ("Mykolaiv", "Mariupol", {"weight": 418}),
        ("Kyiv", "Vinnytsia", {"weight": 267}),
        ("Vinnytsia", "Uzhorod", {"weight": 800}),
        ("Odesa", "Vinnytsia", {"weight": 429}),
    ]
)
