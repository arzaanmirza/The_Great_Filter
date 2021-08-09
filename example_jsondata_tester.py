# This file searches for news articles which relate to Natural Disasters that are occuring in the world.
# It requires you to change the country inputted to which then it finds natural disasters from that country.

#import requests
import json
from newsapi import NewsApiClient


def get_naturaldisaster_news(country_inputted):

    # api = NewsApiClient(api_key='cc17316ba8b84f2eb4aa4d76a6b7d1a5')
    # #country_inputted = 'Japan'    # Country chosen
    # natural_disasters = '(floods OR typhoon OR hurricane OR bushfires OR cyclone OR drought OR rising temperatures OR flooding OR avalanche OR earthquake OR volcano OR heatwave OR famine)' # Natural disaster
    # natural_disasters_list = ["floods","typhoon","hurricane","storm","bushfires","cyclone","drought","heat","rising temperatures","flooding"]
    # #disaster_words = '(kills OR deaths OR destruction)'#disaster words
    #
    # query_string = "("+country_inputted + ' AND ' + natural_disasters+")" #+ ' OR ' + disaster_words # Query statement
    # #news_sources='bbc-news,reuters,abc-news,cnn,foxnews,times-of-india,the-guardian' #All the news sources where you want to search from
    #
    # data = api.get_everything(q=query_string)
    data = {

    "status": "ok",
    "totalResults": 7795,

    "articles": [

        {

            "source": {
                "id": None,
                "name": "Slashdot.org"
            },
            "author": "feedfeeder",
            "title": "The long road to Biden's electric vehicle goal - Axios",
            "description": "The long road to Biden's electric vehicle goalAxios How realistic is President Joe Biden's goal for electric vehicles?CNBC Television How Biden’s E.V. Plan Could Help Tesla and Squeeze ToyotaThe New York Times Opinion | President Biden's electric car plan is …",
            "url": "https://slashdot.org/firehose.pl?op=view&amp;id=149976601",
            "urlToImage": None,
            "publishedAt": "2021-08-07T09:32:27Z",
            "content": "The Fine Print: The following comments are owned by whoever posted them. We are not responsible for them in any way."
        },

        {

            "source": {
                "id": None,
                "name": "Forbes"
            },
            "author": "James Morris, Contributor, \n James Morris, Contributor\n https://www.forbes.com/sites/jamesmorris/",
            "title": "AVA Wants To Put Art And Story Into Electric Vehicles",
            "description": "Electric cars can be a bit boring. AVA's Signature series aims to inject history and even art into each electric vehicle conversion it makes, starting with an AC Cobra boasting an iconic paintjob by Dudley Edwards.",
            "url": "https://www.forbes.com/sites/jamesmorris/2021/08/07/ava-wants-to-put-art-and-story-into-electric-vehicles/",
            "urlToImage": "https://thumbor.forbes.com/thumbor/fit-in/1200x0/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F610d49cf94c952fe27b4e4fd%2F0x0.jpg",
            "publishedAt": "2021-08-07T09:00:00Z",
            "content": "Electric cars have a bit of a problem. Apart from the torque and acceleration compared to internal combustion, they can be a bit boring. Tesla may lead the competition in key areas of technology, but… [+5749 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "Slashdot.org"
            },
            "author": "feedfeeder",
            "title": "Biden loves test-driving fast electric cars, but his snub of Tesla shows he loves unions more - Yahoo News",
            "description": "Biden loves test-driving fast electric cars, but his snub of Tesla shows he loves unions moreYahoo News How realistic is President Joe Biden's goal for electric vehicles?CNBC Television How Biden’s E.V. Plan Could Help Tesla and Squeeze ToyotaThe New York Tim…",
            "url": "https://slashdot.org/firehose.pl?op=view&amp;id=149973237",
            "urlToImage": None,
            "publishedAt": "2021-08-07T07:52:21Z",
            "content": "The Fine Print: The following comments are owned by whoever posted them. We are not responsible for them in any way."
        },

        {

            "source": {
                "id": None,
                "name": "SlashGear"
            },
            "author": "Alvin Reyes",
            "title": "Czinger 21C laps Laguna Seca two seconds faster than McLaren Senna",
            "description": "The Czinger 21C has proven its merits around Laguna Seca Raceway by completing an entire lap two seconds faster than the previous record holder. Piloted by American racing driver Joel Miller, the Czinger 21C has set the fastest lap record at Weathertech Lagun…",
            "url": "https://www.slashgear.com/czinger-21c-laps-laguna-seca-two-seconds-faster-than-mclaren-senna-07685649/",
            "urlToImage": "https://cdn.slashgear.com/wp-content/uploads/2021/08/czinger-21c-9.jpg",
            "publishedAt": "2021-08-07T07:13:42Z",
            "content": "The Czinger 21C has proven its merits around Laguna Seca Raceway by completing an entire lap two seconds faster than the previous record holder. Piloted by American racing driver Joel Miller, the Czi… [+2637 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "CleanTechnica"
            },
            "author": "Jennifer Sensiba",
            "title": "Stellantis: First BEV Jeep Coming In 2023, But What Electric Jeep Will We Get?",
            "description": "A recent Stellantis earnings presentation revealed that Jeep will release its first all-electric vehicle in 2023, and it also revealed various other rough release dates for Stellantis EVs and PHEVs. Sadly, though, the information is still very non-specific. S…",
            "url": "https://cleantechnica.com/2021/08/07/stellantis-first-bev-jeep-coming-in-2023-but-what-electric-jeep-will-we-get/",
            "urlToImage": "https://cleantechnica.com/files/2021/03/jeep-magneto-1.jpg",
            "publishedAt": "2021-08-07T06:43:59Z",
            "content": "A recent Stellantis earnings presentation revealed that Jeep will release its first all-electric vehicle in 2023, and it also revealed various other rough release dates for Stellantis EVs and PHEVs. … [+6108 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "Business Standard"
            },
            "author": "Tara Lachapelle | Bloomberg Opinion",
            "title": "Cash glut at Warren Buffett's Berkshire may trap tech titans next",
            "description": "Unlike some of his ultra-wealthy peers, Buffett still prefers the nuts-and-bolts businesses of Planet Earth",
            "url": "https://www.business-standard.com/article/international/cash-glut-at-warren-buffett-s-berkshire-may-trap-tech-titans-next-121080700344_1.html",
            "urlToImage": "https://bsmedia.business-standard.com/_media/bs/img/article/2021-08/07/full/1628315126-6618.jpg",
            "publishedAt": "2021-08-07T06:02:00Z",
            "content": "Jeff Bezos, since stepping away from Amazon.com Inc., has become the latest billionaire to head to space. Meanwhile, Facebook Inc.’s Mark Zuckerberg is eyeing life in the metaverse. But don’t expect … [+6867 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "Slashdot.org"
            },
            "author": "feedfeeder",
            "title": "How realistic is President Joe Biden's goal for electric vehicles? - CNBC Television",
            "description": "How realistic is President Joe Biden's goal for electric vehicles?CNBC Television How Biden’s E.V. Plan Could Help Tesla and Squeeze ToyotaThe New York Times Biden Aims for 50 Percent New Electric Vehicles by 2030VOA Learning English Opinion | President Biden…",
            "url": "https://slashdot.org/firehose.pl?op=view&amp;id=149967745",
            "urlToImage": None,
            "publishedAt": "2021-08-07T05:12:44Z",
            "content": "The Fine Print: The following comments are owned by whoever posted them. We are not responsible for them in any way."
        },

        {

            "source": {
                "id": None,
                "name": "Livemint"
            },
            "author": "Bloomberg",
            "title": "Warren Buffett and Big Tech are facing this common dilemma. No one knows the answer - Mint",
            "description": "<ol><li>Warren Buffett and Big Tech are facing this common dilemma. No one knows the answer  Mint\r\n</li><li>Warren Buffett’s Cash Trap Can Snare Big Tech, Too  BloombergQuint\r\n</li><li>Warren Buffett sold 'Big Four' airline stocks due to volatility: AA CEO  M…",
            "url": "https://www.livemint.com/companies/people/warren-buffett-and-big-tech-are-facing-this-common-dilemma-no-one-knows-the-answer-11628312244695.html",
            "urlToImage": "https://images.livemint.com/img/2021/08/07/600x338/7afb99351d324770bafc8c5dcec61fcf-7afb99351d324770bafc8c5dcec61fcf-0_1628312874998_1628312899866.jpg",
            "publishedAt": "2021-08-07T05:11:43Z",
            "content": "Jeff Bezos, since stepping away from Amazon.com Inc., has become the latest billionaire to head to space. Meanwhile, Facebook Inc.s Mark Zuckerberg is eyeing life in the metaverse. But dont expect to… [+6004 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "WCNC.com"
            },
            "author": "Brandon Goldner",
            "title": "Gaston County bans mining for 60 days following concerns over proposed lithium mine",
            "description": "The moratorium is aimed directly at Piedmont Lithium, which is pursuing a controversial plan to build an open-pit lithium mine near Cherryville.",
            "url": "https://www.wcnc.com/article/news/local/gaston-county-bans-mining-60-days-concerns-piedmont-lithium/275-ea3729b3-83b2-4513-a9d2-f8c1ce3876db",
            "urlToImage": "https://media.wcnc.com/assets/WCNC/images/3fd9a2c0-9269-400f-828d-0aa6878686bc/3fd9a2c0-9269-400f-828d-0aa6878686bc_1140x641.jpg",
            "publishedAt": "2021-08-07T03:17:21Z",
            "content": "GASTONIA, N.C. Gaston County commissioners voted unanimously Friday to impose a 60-day moratorium on all mining activities in the county.\r\nThe order came as homeowners organized against Piedmont Lith… [+1966 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "24/7 Wall St."
            },
            "author": "247chrislange",
            "title": "Cathie Wood’s ARK Invest Sells for 8/6",
            "description": "Here's a look at the ARK Invest buys for August 6, 2021.",
            "url": "https://247wallst.com/investing/2021/08/06/cathie-woods-ark-invest-sells-for-8-6/",
            "urlToImage": "https://247wallst.com/wp-content/uploads/2018/07/stock-market-financial-data.jpg",
            "publishedAt": "2021-08-07T02:30:54Z",
            "content": "Broad markets cruised higher for the most part on Friday for the most part with the Dow and S&amp;P 500 hitting record highs. However, the Nasdaq and tech sector lagged which did not prove to be a go… [+4360 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "24/7 Wall St."
            },
            "author": "247chrislange",
            "title": "Cathie Wood’s ARK Invest Buys for 8/6",
            "description": "Here's a look at the ARK Invest Buys for August 6, 2021.",
            "url": "https://247wallst.com/investing/2021/08/06/cathie-woods-ark-invest-buys-for-8-6/",
            "urlToImage": "https://247wallst.com/wp-content/uploads/2020/04/imageForEntry1-Qgh.jpg",
            "publishedAt": "2021-08-07T02:26:28Z",
            "content": "The Dow and S&amp;P 500 pushed higherhitting record highsto close out the week while the Nasdaq lagged. A fairly positive July Employment report helped contribute to this rally. However, Cathie Woods… [+5204 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "Motley Fool Australia"
            },
            "author": "James Mickleboro",
            "title": "ASX investors could diversify their portfolios with these quality ETFs",
            "description": "These ETFs could give your portfolio some diversification...\nThe post ASX investors could diversify their portfolios with these quality ETFs appeared first on The Motley Fool Australia.",
            "url": "https://www.fool.com.au/2021/08/07/asx-investors-could-diversify-their-portfolio-with-these-quality-etfs/",
            "urlToImage": "https://www.fool.com.au/wp-content/uploads/2021/05/etf-16_9-1.jpg",
            "publishedAt": "2021-08-07T02:16:30Z",
            "content": "If you wish to add some diversification to your portfolio in August, then you might want to look at exchange traded funds (ETFs).\r\nETFs can help investors achieve diversification with relative ease b… [+1679 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "Yanko Design"
            },
            "author": "Neha Mistry",
            "title": "Top 10 trailer designs of 2021 are here to amp up your summer glamping plans!",
            "description": "Top 10 trailer designs of 2021 are here to amp up your summer glamping plans!It’s time to get back on our bucket list!  After the year of confinement and taking safety precautions, we all have learned and understood the benefits...",
            "url": "https://www.yankodesign.com/2021/08/06/top-10-trailer-designs-of-2021-are-here-to-amp-up-your-summer-glamping-plans/",
            "urlToImage": "https://www.yankodesign.com/images/design_news/2021/08/top-10-trailer-designs-of-2021-are-here-to-amp-up-your-summer-glamping-plans-today-430/Best_Trailer_Designs_2021_outdoor_camping_and_glamping_adventure-23.jpg",
            "publishedAt": "2021-08-07T01:45:35Z",
            "content": "It’s time to get back on our bucket list!  After the year of confinement and taking safety precautions, we all have learned and understood the benefits of traveling – and not just the mindless one. T… [+8983 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "Yahoo Entertainment"
            },
            "author": "James Rubin",
            "title": "Tesla’s Musk Urges Lawmakers Weighing Infrastructure Bill’s Tax Provision Not to Pick Crypto ‘Winners or Losers’",
            "description": "The car company's CEO responded via Twitter to a thread by Coinbase CEO Brian Armstrong, who has been critical of the tax provision and a late amendment to...",
            "url": "https://finance.yahoo.com/news/tesla-musk-urges-lawmakers-weighing-011300764.html",
            "urlToImage": "https://s.yimg.com/uu/api/res/1.2/VszE9Q0xYUAsrkOQHAlxvw--~B/aD0xMDAwO3c9MTUwMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/coindesk_75/06f34df7415ae4c2535eb17aed004192",
            "publishedAt": "2021-08-07T01:13:00Z",
            "content": "Elon Musk urged lawmakers considering the Senate infrastructure bill’s crypto tax provision not “to pick technology winners or losers in cryptocurrency technology” in a tweet responding to Coinbase C… [+1899 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "CleanTechnica"
            },
            "author": "Guest Contributor",
            "title": "How To Improve Storage In A Tesla",
            "description": "By Charles Morris When it comes to storage, Tesla’s vehicles are famous for offering a remarkable amount of space. Not only does each model have a spacious trunk and a frunk, but because the battery pack is placed under the floor pan, a Tesla doesn’t need the…",
            "url": "https://cleantechnica.com/2021/08/06/how-to-improve-storage-in-a-tesla/",
            "urlToImage": "https://cleantechnica.com/files/2021/08/TESLA_MODEL_Y_GARAGE_opendoors_1024x1024.jpeg",
            "publishedAt": "2021-08-07T01:08:49Z",
            "content": "By Charles Morris \r\nWhen it comes to storage, Teslas vehicles are famous for offering a remarkable amount of space. Not only does each model have a spacious trunk and a frunk, but because the battery… [+2570 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "CarScoops"
            },
            "author": "Sebastien Bell",
            "title": "White House May Have Snubbed Tesla At EV Event Because Of Attitude Towards Unions",
            "description": "Tesla's union-busting may have kept it from receiving an invite to the pro-union White House's electrification event.",
            "url": "https://www.carscoops.com/2021/08/white-house-may-have-snubbed-tesla-at-ev-event-because-of-attitude-towards-unions/",
            "urlToImage": "https://www.carscoops.com/wp-content/uploads/2021/08/0x0-Service_09.jpg",
            "publishedAt": "2021-08-07T00:38:47Z",
            "content": "To announce its new plans to push automakers to make 50 percent of their vehicles fully electric by 2030, the White House held a press conference with executives from Ford, GM, and Stellantis. Notabl… [+1713 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "Slashdot.org"
            },
            "author": "feedfeeder",
            "title": "Why Tesla Stock Slipped Today - The Motley Fool",
            "description": "Why Tesla Stock Slipped TodayThe Motley Fool How Biden’s E.V. Plan Could Help Tesla and Squeeze ToyotaThe New York Times President Biden Announces New Electric Car Targets - But Guess Who Wasn't There?Transport Evolved Biden’s new electric car goals are an Ed…",
            "url": "https://slashdot.org/firehose.pl?op=view&amp;id=149960105",
            "urlToImage": None,
            "publishedAt": "2021-08-07T00:33:34Z",
            "content": "The Fine Print: The following comments are owned by whoever posted them. We are not responsible for them in any way."
        },

        {

            "source": {
                "id": None,
                "name": "The Daily Caller"
            },
            "author": "Thomas Catenacci",
            "title": "Biden Administration Approves Rule Forcing Companies To Hire Minority, LGBTQ+ Executives And Publicly Disclose Diversity",
            "description": "The top financial regulatory agency approved a rule that forces publicly-traded companies to reveal the diversity of their executive boardroom to investors.",
            "url": "https://dailycaller.com/2021/08/06/joe-biden-administration-securities-exchange-commission-gary-gensler-nasdaq-diversity/",
            "urlToImage": "https://cdn01.dailycaller.com/wp-content/uploads/2021/08/GettyImages-1231891017-scaled-e1628282442298.jpg",
            "publishedAt": "2021-08-07T00:20:33Z",
            "content": "The top U.S. financial regulatory agency approved a rule that forces publicly-traded companies to reveal the diversity of their executive boardroom to investors.\r\nThe Securities and Exchange Commissi… [+3271 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "ETCanada.com"
            },
            "author": "Jamie Samhan",
            "title": "Vanessa Bryant Settles Lawsuit With Her Mom Over Alleged Unpaid Work",
            "description": "Vanessa Bryant has settled a lawsuit with her mother, Sofia Laine. The terms of the settlement are private, but the lawsuit has been closed with a request for dismissal. In Dec. 2020, Laine filed the lawsuit against her daughter saying she was unpaid despite …",
            "url": "https://etcanada.com/news/807643/vanessa-bryant-settles-lawsuit-with-her-mom-over-alleged-unpaid-work/",
            "urlToImage": "https://etcanada.com/wp-content/uploads/2021/08/GettyImages-1324308288.jpg?quality=80&strip=all&w=720&h=480&crop=1",
            "publishedAt": "2021-08-06T23:49:57Z",
            "content": "By Jamie Samhan.\r\n1 min ago Vanessa Bryant has settled a lawsuit with her mother, Sofia Laine.\r\nThe terms of the settlement are private, but the lawsuit has been closed with a request for dismissal.\r… [+1042 chars]"
        },

        {

            "source": {
                "id": None,
                "name": "Thatsnerdalicious.com"
            },
            "author": "Andrew Cody",
            "title": "Top 10 Best mirror phone mount Reviews",
            "description": "Top 10 Best mirror phone mount in 2021 Comparison Table Are you looking for top 10 great mirror phone mount ... \nRead moreTop 10 Best mirror phone mount Reviews\nThe post Top 10 Best mirror phone mount Reviews appeared first on That's Nerdalicious.",
            "url": "https://thatsnerdalicious.com/top-10-best-mirror-phone-mount-reviews/",
            "urlToImage": "https://m.media-amazon.com/images/I/41vkHdA3w8S._AC_.jpg",
            "publishedAt": "2021-08-06T23:17:50Z",
            "content": "Top 10 Best mirror phone mount in 2021 Comparison Table\r\nBestseller No. 1\r\nHula+ Shower/Mirror Phone Holder/Mount/Stand. Reusable Non-Residue Mount for Bathroom/Kitchen/Wall. Compatible with All Phon… [+15376 chars]"
        }
    ]

}

    list_of_articles = data["articles"]
    list_of_related_articles = []
    count = 0
    for article in list_of_articles:

        title = article["title"]         # Finds the name of the article title
        media_source = article["source"]["name"] # Finds the name of the media source
        article_description = article["description"] #Finds the description of the article
        article_url = article["url"]          #Finds the url of the article


    #This if-statement ensures that the country is in the description
    # of the article, this ensures that the news is from the country inputted.

        # if country_inputted not in article_description:
        #         continue

    # This chunk of code ensures that the article that is picked up by the code actually
    # mentions a natural disaster.
        # word_check=False
        # for word in natural_disasters_list:
        #     if word in article_description:
        #         word_check=True
        #
        # if word_check==False:
        #     continue

    # Printing commands:
        # print(media_source) # Finds the name of the media source
        # print(f"Article Title: {title} ")
        # print(f"Description: {article_description} ")
        # print(f"Article URL: {article_url} ") #Prints the url of the article
        #data = "Media : "+media_source+"\n"+"Article Title: "+title+"\n"+"Description: "+article_description+"\n"+"Article URL: "+article_url
        #print(data)

        data = {

            "Media": media_source,
            "Article Title": title,
            "Description": article_description,
            "Article URL": article_url

        }
        # print(data)
        list_of_related_articles.append(data)

        count = count + 1
        print("\n")

    return list_of_related_articles
#print(count)
