
import random

data = {

    "fire":[
    "https://images.unsplash.com/photo-1473260079709-83c808703435?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=2079&q=80",
    "https://images.unsplash.com/photo-1615092296061-e2ccfeb2f3d6?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1624239843776-bc73d46504bf?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1yZWxhdGVkfDd8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=900&q=60",
    "https://images.unsplash.com/photo-1600297665298-930fd21d3307?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1652&q=80",
    "https://images.unsplash.com/photo-1602065680283-f3e02111a298?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    ],

    "floods":[
    "https://images.unsplash.com/photo-1547683905-f686c993aae5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1612466012988-4f80ea3ea759?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1601231522153-4910f56cb71e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80",
    "https://images.unsplash.com/photo-1599413925144-18ab18fbf223?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80",
    "https://images.unsplash.com/photo-1511894622069-3ed55ebf8f57?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    ],

    "flooding":[
    "https://images.unsplash.com/photo-1547683905-f686c993aae5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1547683905-f686c993aae5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1612466012988-4f80ea3ea759?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1601231522153-4910f56cb71e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80",
    "https://images.unsplash.com/photo-1599413925144-18ab18fbf223?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80",
    "https://images.unsplash.com/photo-1511894622069-3ed55ebf8f57?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    ],


    "flood":[
    "https://images.unsplash.com/photo-1547683905-f686c993aae5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1547683905-f686c993aae5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1612466012988-4f80ea3ea759?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1601231522153-4910f56cb71e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80",
    "https://images.unsplash.com/photo-1599413925144-18ab18fbf223?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1567&q=80",
    "https://images.unsplash.com/photo-1511894622069-3ed55ebf8f57?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    ],


    "heat":[
    "https://images.unsplash.com/photo-1610900743444-21bb7d0fad9a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1622603785487-42552a25c014?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTg2fHxoZWF0JTIwY2l0eXxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
    "https://images.unsplash.com/photo-1470137660724-c60a8b7fc53e?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fGhlYXR8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
    "https://images.pexels.com/photos/68768/sun-setting-sun-sunset-water-68768.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260",
    "https://images.pexels.com/photos/1237119/pexels-photo-1237119.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260",
    ],


    "rain":[
    "https://images.unsplash.com/photo-1513774775025-b2612b7ec096?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1650&q=80",
    "https://images.unsplash.com/photo-1468476396571-4d6f2a427ee7?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1744&q=80",
    "https://images.unsplash.com/photo-1500740516770-92bd004b996e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1652&q=80",
    "https://images.unsplash.com/photo-1513172128806-2d00531a9f20?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fHJhaW55fGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
    "https://images.unsplash.com/photo-1607979035368-f8a53951685b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDJ8fHJhaW55fGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
    ]
}

def image_capture_database(naturaldisaster_article):


    for key in data:


        if key in naturaldisaster_article.lower():
            return random.choice(data[key])


    return "empty_string"
