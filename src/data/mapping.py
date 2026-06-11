feature_points = {
    # Essential value drivers (safety, power, water, parking)
    '24/7 Power Backup': 10,
    'Power Back-up': 10,  
    '24/7 Water Supply': 10,
    'Security Personnel': 9,
    'Car Parking': 9,
    'Visitor Parking': 8,
    'Fire Fighting Systems': 8,
    'Security / Fire Alarm': 8,
    
    # Lifestyle & Premium Amenities
    'Centrally Air Conditioned': 9,
    'Gymnasium': 8,
    'Fitness Centre / GYM': 8,
    'Swimming Pool': 8,
    'Club House': 7,
    'Club house / Community Center': 7,
    'Park': 7,
    "Children's Play Area": 7,
    'Private Garden / Terrace': 8,
    'Low Density Society': 8,
    'Recently Renovated': 7,
    
    # Comfort & Utility Features
    'Internet/wi-fi connectivity': 7,
    'Lift(s)': 8,
    'Rain Water Harvesting': 6,
    'Piped-gas': 6,
    'Water purifier': 6,
    'Maintenance Staff': 6,
    'Waste Disposal': 6,
    'Water Storage': 6,
    'Water softening plant': 6,
    'Spacious Interiors': 7,
    'Natural Light': 6,
    'Airy Rooms': 6,
    'High Ceiling Height': 6,
    
    # Decorative / Niche Features
    'False Ceiling Lighting': 4,
    'Separate entry for servant room': 4,
    'Intercom Facility': 5,
    'InterCom': 5,
    'Bank Attached Property': 4,
    'Shopping Centre': 5,
    'Feng Shui / Vaastu Compliant': 4,
    'No open drainage around': 5
}



city_areas = {
    "Mumbai": [
        "Mumbai", "Andheri", "Malad", "Kandivali", "Chembur", "Borivali", "Goregaon",
        "Mulund", "Santacruz", "Ghatkopar", "Bhandup", "Vikhroli", "Chandivali",
        "Jogeshwari", "Dahisar", "Kurla", "Vile", "Parel", "Dadar", "Kanjurmarg",
        "Bandra", "Sion", "Powai", "Malabar", "Khar", "Vidyavihar", "Govandi",
        "Marol", "Sakinaka", "Kalbadevi", "Shivaji", "Girgaon", "Umerkhadi", "Mahim",
        "Byculla", "Worli", "Dharavi", "Prabhadevi", "Bhuleshwar", "Madh", "Fort",
        "Marine", "Matunga", "Mitha", "Mandvi", "Juhu", "Trombay", "IIT", "MIDC","Cumbala",
        "Lower", "Mankhurd", "New", "Anjur", "Ramabai", "Grant","Asalpha","Maharashtra",
        "Mira", "Naigaon", "Vasai", "Bhayandar", "Nalasopara", "Virar"
    ],
    
    "Thane": [
        "Thane", "Dombivli", "Kalyan", "Ulhasnagar", "Badlapur", "Mumbra",
        "Ambernath", "Ghodbunder", "Manpada", "Bhiwandi", "Titwala", "Kalwa",
        "Majiwada", "Palava"
    ],
    
    "Navi Mumbai": [
        "Navi", "Panvel", "Kalamboli", "Ulwe", "Seawoods", "Uran", "Sanpada",
        "Kharghar", "Airoli", "Belapur", "Nerul", "Neral", "Rasayani", "Vichumbe",
        "Damoji", "Shree","Taloja","Ghansoli"
    ]
}



mapping_area = {
    "Mira-Bhayandar": ["Mira Road", "Shanti Nagar", "Beverly Park", "Mahajan Wadi","mira road"],
    "Dahisar": ["Dahisar","Mandapeshwar", "Rawalpada","Kandarpada",
                "Shailendra Nagar", "Jaya Nagar", "Krishna Colony"],
    "Borivali": ["Borivali",
        "IC Colony", "Shimpoli", "Gorai", "Dahisar Check Naka", "Eksar",
        "Gorai 2", "Babhai", "Chikoowadi", "IC Colony Ext","Rajendra Nagar",
        "Vazira", "Gorai Nagar", "Gorai 3","Yogi Nagar","Sukarwadi"
    ],
    "Kandivali": ["Kandivali","Sai Nagar",
        "Thakur Village", "Lokhandwala Kandivali", "Mahavir Nagar", "Charkop","Babrekar Nagar",
        "Samata Nagar", "Magathane", "Asha Nagar", "Dahanukar Wadi",
        "Sector 5 Charkop", "Sector 6 Charkop", "Sector 3 Charkop", "Sector 8 Charkop",
        "Sector 2 Charkop", "Sector 4 Charkop", "Shankar Pada",
        "Samta Nagar", "Singh Agri Estate", "KANDIVALI WEST"
    ],
    "Malad": ["Malad",
        "Chincholi", "Evershine Nagar", "Jankalyan Nagar", "Orlem", "Marve",
        "Chincholi Bunder", "Dindoshi", "Bangur Nagar","Mahakali Caves",
        "Kurar Village", "Pathan Wadi", "malad west", "Parekh Nagar", "Sunder Nagar"
    ],
    
    "Goregaon": ["Goregaon", "Motilal Nagar 1", "Jawahar Nagar",
        "Film City Road", "Aarey Colony", "Vishveshwar Nagar", 
        "Aarey Milk Colony", "Yashodham", "Royal Palms",
        "goregaon east", "Best Nagar","Siddharth Nagar"
    ],
    "Andheri": ["Andheri", "JVLR",
        "Lokhandwala", "Versova", "Seven Bungalows", "Four Bungalows", "DN Nagar",
        "Veera Desai Road", "JB Nagar", "Poonam Nagar","Sakinaka", "Asalpha",
        "MIDC Chakala Industrial Area", "Gundavali Gaothan","Marol",
        "labh ashish chs andher", "Jp Road","Sher E Punjab Colony"
    ],
    
    "Juhu": ["Juhu", "Silver Beach", "Juhu Scheme","Juhu Tara", "Juhu Lane","Juhu Tara rd"],
    "Vile Parle": ["Vile Parle", "JVPD Scheme", "Jvpd Scheme"],
    "Santacruz": ["Santacruz", "Vakola", "Prabhat Colony", "Vakola Santacruz"],
    "Bandra": ["Bandra","Pali Village",
        "Bandra East", "Bandra West", "Kala Nagar", "Pali Hill"
    ],
    "Dadar": ["Dadar", "Dadar East", "Dadar West","Lokmanya Tilak Colony", "Shivaji Park", "Hindu Colony" ],
    "Wadala": ["Wadala", "Antop Hill"],
    "Worli": ["Worli", 
        "Prabhadevi", "Upper Worli", "Worli Naka",
        "Gandhi Nagar Worli", "Old Prabhadevi"
    ],
    "Parel":["Parel","Lower Parel","Mahalaxmi","Agar Bazar"],
    "Churchgate":["Sonapur"],
    "Kurla": ["Kurla", "Jagruti Nagar"],
    "Chembur": ["Chembur", 
        "Deonar", "Tilak Nagar", "Ghatla", "RCF Colony Chembur",
        "Collector Colony", "Chedda Nagar", "Swastik Park", "Deonar Municipal Colony",
        "Union Park", "Sindhi Society Chembur"
    ],
    "Ghatkopar": ["Ghatkopar", "Pant Nagar", "Garodia Nagar", "Barve Nagar",
                "Sainath Nagar","Maneklal Estate", "Amrut Nagar", "Ramabai Colony"],
    "Vikhroli": ["Vikhroli", 
        "Kannamwar Nagar 1", "Kannamwar Nagar 2", "Vikhroli Park Site", "Parksite Colony",
        "Hariyali", "Vikhroli Village"
    ],
    "Powai": ["Powai",
        "Hiranandani Gardens", "IIT", "Chandivali", "Tunga Village",
        "Panchkutir Ganesh Nagar", "Nahar Amrit Shakti", "Sangharsh Nagar",
        "Hiranandani Estate", "Raheja Vihar", "Lok Milan Colony"
    ],
    "Bhandup": ["Bhandup", "Jaydev Nagar", "Nahur", "Valmiki Nagar", "Battipada", "Jaydev Singh Nagar"],
    "Mulund": ["Mulund", "Gavanpada", "Jaihind Colony", "Deendayal Nagar",
        "Veena Nagar", "Nahur Gaothan", "Vardhman Nagar", "Gavane Pada Mulund"
    ],
    
    "Kanjurmarg": ["Kanjurmarg", "Kanjurmarg west"],
    "Vidyavihar": ["Vidyavihar", "Vidya Nagari","Kirol Village"],
    "Sion": [ "Sion", "GTB Nagar", "Pratikhsha Nagar"],
    "Mankhurd": ["Mankhurd", "Govandi"],
    "Thane": ["Thane", "Veer Savarkar Nagar", "Chatrapati Shivaji Nagar"
        "Panch Pakhadi", "Naupada", "Vasant Vihar", "Kopri", "Vartak Nagar",
        "Brahmand", "Kavesar", "Waghbil", "Dhokali", "Hiranandani Meadows",
        "Kapurbawadi", "Ambernath", "Kharegaon", "Datta Chowk","Kharvai",
        "Kasar vadavali","Ulhasnagar", "Manpada","Majiwada","Badlapur",
        "Kolshet Road","Pokhran 2","Balkum","Shahad", "Dahisar Mori"
    ],
    "Kalyan-Dombivli": ["Kalyan-Dombivli",
        "Thakurli", "Adharwadi", "Hanuman Nagar",
        "Ambernath", "Katemanivali", "Tukaram Nagar"
    ],
    "Mumbra": ["Kausa", "Mumbra"],
    "Diva": ["Diva"],   
    
    
    
    "Colaba": ["Colaba", "Cuffe Parade", "Nariman Point"],
    "Girgaon-Malabar": ["Girgaon", "Walkeshwar", "Malabar Hill", "Babulnath", "Chira Bazaar",
                 "Dhobi Talao", "Mohamed Ali Road", "Kumbharwada", "Cawasji Patel Tank","Gaiwadi", "Prathna Samaj"],
    "Grant Road": ["Grant Road"],
    "Agripada": ["Agripada", "Agripada", "Jacob Circle"],
    "Byculla": ["Byculla", "Madam Cama", "Chinchpokli", "Sane Guruji Nagar", "Umerkhadi", "Mustafa Bazar"],
    "Byculla-Mazgaon": ["Byculla-Mazgaon", "Sandhurst Road", "Lalbaug"],
    "Mazgaon-Chinchpokli": ["Mazgaon-Chinchpokli", "Mazgaon", "Chinchpokli"],
    "Mandvi-Bhuleshwar": ["Mandvi-Bhuleshwar", "Mandvi", "Bhuleshwar"],





    "Airoli": ["Airoli", "Sector 2 Airoli", "Sector 4 Airoli", "Sector 20B Airoli"],
    "Vashi": ["Vashi", "Sector 6 Vashi", "Sector 28 Vashi"],
    "Sanpada": ["Sanpada"],
    "Nerul": ["Nerul", 
        "Sector 17 Nerul", "Sector 27 Nerul", "Sector 21 Nerul", "Sector 28 Nerul",
        "Sector 19A Nerul", "Sector 18A Nerul"
    ],
    "Seawoods": ["Seawoods", "Sector 40 Seawoods"],
    "Belapur": ["Belapur", "Agroli","Sector 30 Belapur", "Sector 19 Belapur"],
    "Kharghar": ["Kharghar", 
        "Sector 35G Kharghar", "Sector 12 Kharghar", "Sector 35D Kharghar", "Sector 35I Kharghar",
        "Sector 34C Kharghar", "Sector 21 Kharghar", "Sector 19 Kharghar", "Sector 35E Kharghar",
        "Sector 23 Kharghar", "Sector 20 Kharghar", "Sector 15 Kharghar", "Sector 5 Kharghar",
        "Sector 7 Kharghar","Sector 6 Kharghar","Sector 34 Kharghar", "Sector 34A Kharghar", "Sector 34B Kharghar",
        "Sector 13 Kharghar", "Sector 10 Kharghar", "Sector 4 Kharghar",
        "Block G Sector 12 Kharghar", "Sector 18 Kharghar", "Sector 27 Kharghar"
    ],
    
    "Kamothe": ["Kamothe", "Sector 22 Kamothe", "Sector 21 Kamothe", "Sector 19 Kamothe", "Sector 18 Kamothe"],
    "Ulwe": ["Ulwe", "Sector 8 Ulwe", "Sector 5 Ulwe", "Sector 2 Ulwe", "Pushpak Nagar", "Sector 20 Ulwe", "Sector 16 Ulwe"],
    "Kalamboli": ["Kalamboli"],
    "Taloja": ["Taloja", "Taloja Panchanand", "Sector 24 Taloja"],
    "Roadpali": ["Roadpali", "Sector 17 Roadpali", "Sector 20 Roadpali"],
    "Panvel": ["Panvel", "Old Panvel", "Sector 6 New Panvel", "Sector 10 New Panvel"],
    "Sandhurst": ["Sandhurst", "Sandhurst Road"],
    
    
    
    
    
    "Others": ["Gandhi Nagar","Netaji Nagar","Shivaji Nagar",
        "Mumbai", "Friends Colony", "Jai Jawan Nagar", "Panchsheel Nagar",
        "Agashi", "Postal Colony", "Khalai Village", "Vadavali", "Khardi", "Boisar",
        "Industrial Area", "Hallow Pul", "Karve Nagar", "Paranjape Nagar", "Mahesh Nagar", "Link Road",
        "Sen Nagar", "Chandan Shanti", "Vithal Nagar", "Miragaon", "Kamlakar Nagar",
        "Phoolpada Road", "Gamdevi", "Kevni Pada", "Phase 7 Geeta Nagar", "Sriprastha",
        "Kemps corner", "Navghar", "Rayani Gram", "Ghodapdeo", "Yamuna Nagar",
        "Jai Hind Nagar", "Tanji Nagar", "Neral matheran", "Lal Bahadur Shastri Nagar",
        "Jijamata Colony", "Sriprastha", "Mbh Colony", "Jagjivan Ram Nagar", "Pereira Wadi",
        "Potohar Nagar", "New Link Road", "Save Nagar", "Babulnath",
        "Shanti Vihar", "Umershetpada", "Maratha Colony",
        "sunny road", "DGQA Colony", "Brahmanwadi", "Mahatma Jyotiba Phule Nagar",
        "share punjab", "Sathi D Souza Nagar", "Mohananad Nagar",
        "Dhaku Prabhuchi Wadi", "Navy Colony", "Halav Pool", "Meghwadi", "Dina Bama Estate",
        "Vishwakarma Nagar", "Mahalaxmi Sindhi Colony", "Unique Gardens", "Kunchi Kurve Nagar",
        "Gaurishankar Wadi", "Saraswati Baug", "Masjid Bandar", "Shree Ram Nagar",
        "coral", "Neelkanthnagar", "Asavari", "Sabale Nagar", "RBI Staff Colony",
        "Dattaguru Nagar", "Kanjur Village", "Nensey Colony", "Bhadwad", "Nandkar",
        "407"
    ]
}


mapping_area.update({
    "Vasai-Virar": ["Vasai-Virar","nallasopara",'Virar', "virar east", "nalasopara east", "Dongarpada", "Pelhar", 
            "Baneli", "Chinch Aali", "Joveli Gaon","Vasai","Kanchpada","Naigaon", "Nalasopara", "Uttan",
            "virar west", "HDIL layout chikaldongari virar west"],
    "Mira-Bhayandar": mapping_area["Mira-Bhayandar"] + ["Kashimira","Bhayandar",
        "Shyam Nagar", "Naya Nagar", "Beverly Park", "Mithchowki",
        "Near GCC Club", "Poonam Sagar Complex", "Kashigaon", "Medetiya Nagar"],
    "Borivali": mapping_area["Borivali"] + [
        "Gorai 1", "Yashavant Nagar", "Haridas Nagar", "Ramgad Nagar", "Dongripada",
        "Star Colony", "Kamathi Wada", "Gavraipada", "Bhimnagar",
        "Navapada", "Rambaug", "Dattani Nagar", "Samrat Ashok Nagar","Churi Wadi"
    ],
    "Kandivali": mapping_area["Kandivali"] + [ "Sector 7 Kandivali", "Sector 9 Charkop", "Akurli Nagar", "Ashok Nagar Kandivali", 
        "Pai Nagar", "Pushpa Park", "Unnat Nagar", "Unnat Nagar 2", "Kanakia Park", "Kanakiya", "Kulupwadi", "Kandivali west",
        "Motilal Nagar 3", "Loknagari","Thakur complex","Sector 1 Charkop" ],

    "Malad": mapping_area["Malad"] + [
        "Irani Wadi", "Liberty Garden", "Mitha Nagar", "Rathodi", "Malpa Dongri", "Shankarwadi",
        "Kharodi Naka", "Chinchodyacha Pada","Marve Village", "Milat Nagar", "Phase 4 Jankalyan Nagar",
        "Azad Nagar", "Malvani", "Mindspace", "Kastur Park", "Marve Road"
    ],
    "Goregaon": mapping_area["Goregaon"] + ["Suchi Dham", "Swami Samarth Nagar", "Pimpripada","Nadiyawala Colony 2",
                                            "Gokuldham Colony"],
    "Jogeshwari":["Oshiwara","Behram Baug","Natwar Nagar", "Jogeshwari"],
    "Andheri": mapping_area["Andheri"] + [
        "Aram Nagar", "Aram Nagar Part 1", "Versova Village", "Irla", "Chuim Village",
        "Andheri kamala co operative housing society off j p road opp Navrang Cinema",
        "Kondivita", "Sahar", "Nl Complex", "Lokhandwala Andheri", "Amboli", "Anand Nagar", "Chakala",
        "Ashok Nagar", "Yari Road"
    ],
    "Santacruz": mapping_area["Santacruz"] + ["Shivaji nagar Vakola", "Kolivery Village","SV Road","Shivaji Nagar","Kalina"],
    "Bandra": mapping_area["Bandra"] + ["Band Stand", "Reclamation","Bandra Kurla Complex", "Seven Bunglow"],
    "Dadar": mapping_area["Dadar"] + [
        "Saraswat Colony", "Century Bazaar", "Bhawani Sankar"
    ],
    "Khar": ["Ram Krishna Nagar","Khar"],
    "Mahim":["Mahim"],
    "Worli": mapping_area["Worli"] + [
        "BDD Chawls Worli", "Senapati Bapat Marg", "Delisle road", "Century Bazaar",
        "Mahalaxmi Railway Station", "Haji Ali"
    ],
    "Matunga":["Joshi vadi", "Matunga"],
    "Kurla": mapping_area["Kurla"] + ["nerul nagar kurla east", "Qureshi Nagar", "Netaji Subhash Nagar","Mata Ramabai Ambedkar Nagar", "Lallubhai Compound"],

    "Chembur": mapping_area["Chembur"] + [
        "Baiganwadi", "Chembur Gaothan", "Borla", "Barve Nagar", "RCF BARC Colony", "Bhakti Park","Pestom Sagar Colony"
    ],
    "Ghatkopar": mapping_area["Ghatkopar"] + [
        "Rajawadi Colony", "Pant Nagar", "Ramabai Ambedkar Nagar"
    ],
    "Vikhroli": mapping_area["Vikhroli"] + ["Tagore Nagar", "Ekvira Darshan","Nehru Nagar"],
    "Powai": mapping_area["Powai"] + ["IIT Area",'Hiranandani Gardens Powai',"BMC Colony"],
    "Bhandup": mapping_area["Bhandup"] + ["Sheshwadi", "Tulshetpada","Gavane Pada", "Datar Colony"],
    "Mulund": mapping_area["Mulund"] + ["Vatsalabai Naik Nagar", "Vasant Oscar", "Akurli","Khindipada","Mulund Colony"],
    "Sion": mapping_area["Sion"] + ["Sion Trombay Road", "Sion Koliwada"],
    "Mankhurd": mapping_area["Mankhurd"] + ["Trombay", "Mysore Colony"], 
    "Khanda Colony": ["Khanda Colony", "Sector 4A Khanda Colony", "Sector 5 Khanda Colony", "Greater Khanda", "Sector 11 Khanda Colony",
                      "Sector 17 Khanda Colony"],

    "Thane": mapping_area["Thane"] + ["Uthalsar", "Gawand Baug", "Louis Wadi", "Balkum Naka", "Dhokali", "Goddev Village", 
                                      "khopat", "Kolshet", "Kolbad", "Yogidham", "Gaodevi","Gundavali", "Titwala", "Ghodbunder Road", "Khadakpada", "Pokharan Road",
                "Shastri Nagar", "Shastri Nagar ", "Chikhal Dongari", "Laxmi Nagar","Pirojshanagar", "Daulat Nagar", "Dattapada", "Upper Govind Nagar",
        "Mhada Colony", "Madh", "Shilphata", "Adarsh Nagar", "Hatkesh Udhog Nagar","Moti Nagar", "Kalwa", "Shahapur", "SV Patel Nagar", "Ambedkar Nagar",
        "Subhash Nagar", "Chirag Nagar", "Anjurdive", "Ramdev Park", "Alika Nagar","Gangawadi", "Kasam Baug", "Lal Baug", "Tambe Nagar", "Gaon Devi",
        "Bhatwadi", "Savarkar Nagar", "Bhadran Nagar", "Nirmal Nagar", "Devipada","Ganesh Nagar", "Navagaon", "LIC Colony", "Vinay Nagar", "Vaishali Nagar",
        "Hanuman Chowk", "Chanakya Nagar", "Somwari Bazar", "Tata Colony","Yashwant Nagar", "Teen Hath Naka", "Tembhipada", "Mahadeo Wadi","Pratap Nagar"],

    "Kalyan-Dombivli": mapping_area["Kalyan-Dombivli"] + ["Dombivli",
        "Beturkar Pada", "Katrap", "Sagaon", "Wayle Nagar", "Tisgaon", "Hendre Pada",
        "Varap", "Ambika Nagar", "Nilje Gaon", "Manda", "Nevali", "Charai", "Godrej hill",
        "Kachore Gaon", "Vithalwadi", "Rambaug", "Dombivli Manpada", "Kulgaon", "Shiv Shakti Nagar",
        "Ambivli", "KALYAN Bhiwandi BYPAS", "Kolsewadi", "Dwarli Pada", "Dawadi Gaon",
        "Ayodhya Nagari", "Dhakate Shahad", "Annapurna Nagar",
        "Dahivali", "Mariam Nagar", "Kopar", "Usarghar Gaon",
        "dombivli west", "KALYAN Bhiwandi BYPASS"
    ],
    "Mumbra": mapping_area["Mumbra"] + ["Mumbra Station"],
    "Bhiwandi": ["Bhiwandi", "Mankoli", "Narpoli"],
    "Karjat":["Karjat"],




    "Colaba": mapping_area["Colaba"] + ["Colaba", "Cumbala Hill", "Peddar Road", "Breach Candy"],
    "Girgaon":# mapping_area["Girgaon"] +
      [
        "Thakurdwar", "Dongri", "Marine Lines", "Marine Drive", "Napean Sea Road"
    ],
    "Mazgaon": #mapping_area["Mazgaon"] + 
    ["Dongri", "Chinchbunder"],
    "Byculla": mapping_area["Byculla"] + ["Nagpada", "Kamathipura", "Reay Road","Tardeo","Sewri"],

    "Cumbala Hill": ["Cumbala Hill", "Peddar Road", "Cumbala Hill", "Breach Candy"],    
    



    "Airoli": mapping_area["Airoli"] + ["Sector 6 Airoli", "Sector 2B Airoli", "Sector 8A Airoli", "Sector 8 Airoli", "Sector 20 Airoli", "Sector 19 Airoli",
        "Sector 9 Airoli", "Sector 16 Airoli"],
    "Ghansoli": ["Ghansoli","Sector 30 Ghansoli", "Sector 16 Ghansoli","Sector 4 Ghansoli", "Sector 21 Ghansoli", "Sector 15 Ghansoli",
        "Sector 11 Ghansoli", "Sector 23 Ghansoli", "Sector 2 Ghansoli"],
    "Vashi": mapping_area["Vashi"] + [
        "Sector 29 Vashi", "Sector 12 Vashi", "Sector 7 Vashi", "Sector 14 Vashi",
        "Sector 4 Vashi", "Sector 10 Vashi", "Sector 16 Vashi", "Sector 8 Vashi", "Sector 10A Vashi","Sector 16 Vashi (dup)", 
        "Sector 8 Vashi (dup)", "Sector 4 Vashi (dup)", "Sector 6 Vashi (dup)", "Sector 28 Vashi (dup)", "Sector 10 Vashi (dup)"
    ],
    "Sanpada": mapping_area["Sanpada"] + ["Sector 4 Sanpada","Sector 5 Sanpada"],
    "Nerul": mapping_area["Nerul"] + ["Sector 9 Nerul", "Sector 23 Nerul", "Sector 10 Nerul","Sector 16 Nerul", "Sector 16A Nerul",
                                       "Sector 18 Nerul", "Sector 19 Nerul", "Sector 29 Nerul", "Sector 1 Shiravane"],
    "Seawoods": mapping_area["Seawoods"] + ["Sector 58 Seawoods", "Sector 50 Seawoods", "Sector 42 Seawoods", "Nerul Seawoods Sector 40"],
    "Belapur": mapping_area["Belapur"] + ["Sector 15 Belapur", "Sector 29 Belapur"],
    "Kamothe": mapping_area["Kamothe"] + [
        "Sector 15 Kamothe", "Sector 20 Kamothe", "Sector 36 Kamothe", "Sector 11 Kamothe",
        "Sector 17 Kamothe", "Sector 24 Kamothe", "Sector 10 Kamothe",
        "Sector 34 Kamothe", "Sector 9 Kamothe","Sector 35 Kamothe"
    ],
    "Ulwe": mapping_area["Ulwe"] + ["Sector 21 Ulwe", "Sector 23 Ulwe", "Sector 3 Ulwe", "Sector 19B Ulwe", "Sector 19 Ulwe",
                            "Sector 9 Ulwe", "Sector 17 Ulwe", "Sector 18 Ulwe"],
    "Kalamboli": mapping_area["Kalamboli"] + ["Sector 8 Kalamboli"],
    "Taloja": mapping_area["Taloja"] + ["Sector 20 Taloja", "Sector 26 Taloja Phase 2", "Taloja Phase 2", "Sector 37 Taloja", "Sector 16 Taloja"],
    "Panvel": mapping_area["Panvel"] + [
        "Sector 5 New Panvel", "Sector 3 New Panvel", "Sector 11 New Panvel", "Sector 13 New Panvel", "new panvel",
        "Taloja Phase 1", "Taloja Phase 2", "Navade", "Sukapur", "Panvel", "Devad", "Cidco Colony", "Pushpak Nagar",
        "Sector 12 New Panvel", "Palaspe Phata"
    ],
    "Turbhe": ["Turbhe", "Turbhe MIDC"],
    "Navi Mumbai":["Kopar Khairane", "Vichumbe", "Sector 25 Khandeshhwar"],




    
    "Mumbai":["Dharavi","Chunabhatti","Tirupati Nagar Phase 2", "Shivai Nagar", "Golibar", "Kapadia Nagar",
        "Air Force Quarters", "Sag Baug", "Mohili", "Kherwadi", "Bhoiwada", "Opera House",
        "Nadiyawala Colony 1", "Ashok Van", "Adarsh Dugdhalaya", "New Rajaram Wadi",
        "Parmanand Wadi", "Abhyudaya Nagar", "Jethava Nagar", "Kajupada",
        "Siddheshwar Nagar", "Ram Nagar", "Parbat Nagar", "Chikuwadi",
        "Mohite Wadi", "Vijaykar Wadi", "Bhavani Nagar", "Santosh Nagar",
        "Anita Nagar", "Motilal Nagar 2", "Kamgar Nagar", "Devripada",
        "Garibachawada", "Kadamwadi", "Poonam Gardens", "Buwapada",
        "MIDC Residential Area", "Sardar Vallabhbhai Patel Nagar", "Tolaram Colony",
        "Kranti Nagar", "Phase 2", "Ekta Nagar", "Gaikwad Nagar", "MIDC",
        "Mumbai Nashik Highway", "Govardhan Nagar", "Ghartan Pada", "Kailash Colony",
        "Jay Prakash Nagar", "Kolshet Industrial Area", "Gautam Nagar", "Piramal Nagar",
        "Kailash Nagar", "Kamala Nagar", "Sanjay Nagar", "Narayan Nagar",
        "Jari Mari", "Khira Nagar", "Saki Vihar", "JK Gram", "Parsi Wada",
        "Parshiwadi Varachi", "Lokmanya Nagar", "Harbadevi", "Ratan Nagar",
        "Chittranjan Nagar", "Divya Park", "BARC", "Kharodi Village", "Bafhira Nagar",
        "Manisha nagar", "Hari Om Nagar", "Khadavali", "Desale Pada", "Rajawadi",
        "Fish Market Area", "Pathan Colony", "Khetwadi", "Sagar City",
        "Narayan Nagar Ghatkopar west", "Sector 3 Shanti Nagar", "Gulmohar Colony",
        "Juni", "Samel Pada", "Panchamratna Park", "Shirdi Nagar", "Sunil Nagar"],
    "Others": mapping_area["Others"] + [
        "Asangaon", "Dronagiri", "Bolinj", "Owale", "Kasheli", "Pranay Nagar", "Vishnu Nagar", "Parsik Nagar ",
        "Navneeth Colony", "Hira Nagar", "Indralok Phase 6", "Vivekanand Nagar", "Adai", "Sopara", "Sidhi Vinayak Nagar",
        "Kegaon", "Naka", "Parsi Colony", "Petali", "Kongaon", "Karade Khurd", "Vasind", "Ushma Nagar", "Bhaskar Colony",
        "Gaondevi Dongri", "Maharashtra Nagar", "Naidu Colony", "Bhayandarpada", "Patlipada", "Rajiv Gandhi Nagar",
        "Govind Nagar", "Neelam Nagar", "Sindhu Wadi", "Khar Kopar", "Khatiwali", "Jambhulpada", "Ambivali", "Wagholi",
        "Mothagaon", "Sonivali", "lonavala", "Casa Bella", "Chinchoti", "Palm Beach", "HMPL Surya Nagar", "Padma Nagar",
        "Sadan wadi", "Yashaswi Nagar", "Shirgaon", "Sarvodaya Nagar", "Sambhaji Nagar", "Mira Gaothan", "Lamington Road",
        "Ajit Nagar", "Siddharath Nagar", "New Mhada Society", "Kokan Nagar", "Kanakiya", "Mamletdar Wadi", "Bharat Nagar",
        "Meghdoot", "Brahmanwada", "Sindhu Nagar", "Shri Nagar", "Savitribai Phule Nagar", "Dev Nagar", "Vijay Nagar",
        "Kumud Nagar", "Golani Naka", "Nilemore", "CST", "Laxman Nagar", "Gandhar Nagar", "Sonar Pada", "Naringi",
        "Shidivinayak Colony", "Jijamata Nagar", "Shaninagar", "Indira Nagar", "Savoli", "Ganga Vihar", "Sagarli",
        "Krishna Park", "Muthaval", "Mirashi Nagar", "kalyan", "Bhagat Colony", "Khoni",
        "Sindhu Cementers Tavisa", "Old Zakat Naka", "Panjarpole", "Hind Nagar", "Shahabaj", "on request", "Waliv",
        "Papdi", "Mukund Nagar", "bhakti homes", "Arya Nagar", "Mulgaon", "Vajreshwari", "Jui", "Swanand Nagar",
        "Shailesh Nagar", "Katai Naka", "Jawsaigaon", "Dhobi Ali", "lakhander", "Ambadi Naka", "Inamdar Wada",
        "Arunoday Nagar", "Dhuru Wadi", "Fisherman colony", "Ambewadi", "Murdha", "Mahapoli", "Manera Gaon",
        "107 anandnagar", "Potgaon", "Adaigaon", "Wadeghar", "Sai Gaon", "Dionna", "Manohar Nagar", "Vithaldas Nagar",
        "Dawood Baug", "Nav Indraprastha CHS", "MMRDA Area", "Aptewadi", "Nav Pada", "Nane Pada", "Jai Ambe Nagar",
        "Barrister Nath Pai Nagar", "Chandrakant Dhuru Wadi", "nilemore nallasa", "Vijay Park", "Safed Pul", "VSNL Colony",
        "Suresh Nagar", "Dhakoji Sethpada", "New Gautam Nagar", "Shantivan", "Sindhi Colony", "Central Area",
        "Khandelwal Layout", "Mangal Nagar", "Xo chs", "Ghotkamp Koyana Vele", "luna wala", "Waliv Phata", "Pawan Baug",
        "Sector 14 Kalamboli", "Juhu Circle", "OT Section", "lurbanum road",
        "Yagna Nagar", "Anand Koliwada", "Maratha Section 32", "Saraswat Nagar", "Surai", "Amar Nagar", "Housing Board Colony",
        "Chinchpada Gaon", "Wahal", "Midc Colony", "Khardev Nagar", "Bhivpuri"
    ]
})
