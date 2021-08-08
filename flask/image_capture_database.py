
data = {

    "fire":"https://images.unsplash.com/photo-1473260079709-83c808703435?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2079&q=80",
    "floods":"https://images.unsplash.com/photo-1547683905-f686c993aae5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "flooding":"https://images.unsplash.com/photo-1547683905-f686c993aae5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "flood":"https://images.unsplash.com/photo-1547683905-f686c993aae5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "heat":"https://images.unsplash.com/photo-1610900743444-21bb7d0fad9a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "rain":"https://images.unsplash.com/photo-1513774775025-b2612b7ec096?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",

}

def image_capture_database(naturaldisaster_article):


    for key in data:


        if key in naturaldisaster_article.lower():
            return data[key]


    return "empty_string"
