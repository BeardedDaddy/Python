import csv

medals_table = [
    {'country': 'United States'},
    {'country': 'United States', 'gold': 39},
    {'country': 'United States', 'gold': 39, 'silver': 41},
    {'country': 'United States', 'gold': 39, 'silver': 41, 'bronze': 33},
    {'country': 'United States', 'gold': 39,
        'silver': 41, 'bronze': 33, 'rank': 1},
]

    {'country': 'China'},
    {'country': 'China', 'gold': 38},
    {'country': 'China', 'gold': 38, 'silver': 32},
    {'country': 'China', 'gold': 38, 'silver': 32, 'bronze': 18},
    {'country': 'China', 'gold': 38, 'silver': 32, 'bronze': 18, 'rank': 2},
]

    {'country': 'Japan'},
    {'country': 'Japan', 'gold': 27},
    {'country': 'Japan', 'gold': 27, 'silver': 14},
    {'country': 'Japan', 'gold': 27, 'silver': 14, 'bronze': 17},
    {'country': 'Japan', 'gold': 27, 'silver': 14, 'bronze': 17, 'rank': 3},
]

    {'country': 'Great Britain'},
    {'country': 'Great Britain', 'gold': 22},
    {'country': 'Great Britain', 'gold': 22, 'silver': 21},
    {'country': 'Great Britain', 'gold': 22, 'silver': 21, 'bronze': 22},
    {'country': 'Great Britain', 'gold': 22,
        'silver': 21, 'bronze': 22, 'rank': 4},
]

    {'country': 'ROC'},
    {'country': 'ROC', 'gold': 20},
    {'country': 'ROC', 'gold': 20, 'silver': 28},
    {'country': 'ROC', 'gold': 20, 'silver': 28, 'bronze': 23},
    {'country': 'ROC', 'gold': 20, 'silver': 28, 'bronze': 23, 'rank': 5},
]

    {'country': 'Australia'},
    {'country': 'Australia', 'gold': 17},
    {'country': 'Australia', 'gold': 17, 'silver': 7},
    {'country': 'Australia', 'gold': 17, 'silver': 7, 'bronze': 22},
    {'country': 'Australia', 'gold': 17, 'silver': 7, 'bronze': 22, 'rank': 6},
]

    {'country': 'Netherlands'},
    {'country': 'Netherlands', 'gold': 10},
    {'country': 'Netherlands', 'gold': 10, 'silver': 12},
    {'country': 'Netherlands', 'gold': 10, 'silver': 12, 'bronze': 14},
    {'country': 'Netherlands', 'gold': 10, 'silver': 12, 'bronze': 14, 'rank': 7},
]

    {'country': 'France'},
    {'country': 'France', 'gold': 10},
    {'country': 'France', 'gold': 10, 'silver': 12},
    {'country': 'France', 'gold': 10, 'silver': 12, 'bronze': 11},
    {'country': 'France', 'gold': 10, 'silver': 12, 'bronze': 11, 'rank': 8},
]

    {'country': 'Germany'},
    {'country': 'Germany', 'gold': 10},
    {'country': 'Germany', 'gold': 10, 'silver': 11},
    {'country': 'Germany', 'gold': 10, 'silver': 11, 'bronze': 16},
    {'country': 'Germany', 'gold': 10, 'silver': 11, 'bronze': 16, 'rank': 9},
]

    {'country': 'Italy'},
    {'country': 'Italy', 'gold': 10},
    {'country': 'Italy', 'gold': 10, 'silver': 10},
    {'country': 'Italy', 'gold': 10, 'silver': 10, 'bronze': 20},
    {'country': 'Italy', 'gold': 10, 'silver': 10, 'bronze': 20, 'rank': 10},
]

    {'country': 'Canada'},
    {'country': 'Canada', 'gold': 7},
    {'country': 'Canada', 'gold': 7, 'silver': 6},
    {'country': 'Canada', 'gold': 7, 'silver': 6, 'bronze': 11},
    {'country': 'Canada', 'gold': 7, 'silver': 6, 'bronze': 11, 'rank': 11},
]

    {'country': 'Brazil'},
    {'country': 'Brazil', 'gold': 7},
    {'country': 'Brazil', 'gold': 7, 'silver': 6},
    {'country': 'Brazil', 'gold': 7, 'silver': 6, 'bronze': 8},
    {'country': 'Brazil', 'gold': 7, 'silver': 6, 'bronze': 8, 'rank': 12},
]

    {'country': 'New Zealand'},
    {'country': 'New Zealand', 'gold': 7},
    {'country': 'New Zealand', 'gold': 7, 'silver': 6},
    {'country': 'New Zealand', 'gold': 7, 'silver': 6, 'bronze': 7},
    {'country': 'New Zealand', 'gold': 7, 'silver': 6, 'bronze': 7, 'rank': 13},
]

    {'country': 'Cuba'},
    {'country': 'Cuba', 'gold': 7},
    {'country': 'Cuba', 'gold': 7, 'silver': 3},
    {'country': 'Cuba', 'gold': 7, 'silver': 3, 'bronze': 5},
    {'country': 'Cuba', 'gold': 7, 'silver': 3, 'bronze': 5, 'rank': 14},
]

    {'country': 'Hungary'},
    {'country': 'Hungary', 'gold': 6},
    {'country': 'Hungary', 'gold': 6, 'silver': 7},
    {'country': 'Hungary', 'gold': 6, 'silver': 7, 'bronze': 7},
    {'country': 'Hungary', 'gold': 6, 'silver': 7, 'bronze': 7, 'rank': 15},
]

    {'country': 'South Korea'},
    {'country': 'South Korea', 'gold': 6},
    {'country': 'South Korea', 'gold': 6, 'silver': 4},
    {'country': 'South Korea', 'gold': 6, 'silver': 4, 'bronze': 10},
    {'country': 'South Korea', 'gold': 6, 'silver': 4, 'bronze': 10, 'rank': 16},
]

    {'country': 'Poland'},
    {'country': 'Poland', 'gold': 4},
    {'country': 'Poland', 'gold': 4, 'silver': 5},
    {'country': 'Poland', 'gold': 4, 'silver': 5, 'bronze': 5},
    {'country': 'Poland', 'gold': 4, 'silver': 5, 'bronze': 5, 'rank': 17},
]

    {'country': 'Czech Republic'},
    {'country': 'Czech Republic', 'gold': 4},
    {'country': 'Czech Republic', 'gold': 4, 'silver': 4},
    {'country': 'Czech Republic', 'gold': 4, 'silver': 4, 'bronze': 3},
    {'country': 'Czech Republic', 'gold': 4, 'silver': 4, 'bronze': 3, 'rank': 18},
]

    {'country': 'Kenya'},
    {'country': 'Kenya', 'gold': 4},
    {'country': 'Kenya', 'gold': 4, 'silver': 4},
    {'country': 'Kenya', 'gold': 4, 'silver': 4, 'bronze': 2},
    {'country': 'Kenya', 'gold': 4, 'silver': 4, 'bronze': 2, 'rank': 19},
]

    {'country': 'Norway'},
    {'country': 'Norway', 'gold': 4},
    {'country': 'Norway', 'gold': 4, 'silver': 2},
    {'country': 'Norway', 'gold': 4, 'silver': 2, 'bronze': 2},
    {'country': 'Norway', 'gold': 4, 'silver': 2, 'bronze': 2, 'rank': 20},
]

    {'country': 'Jamaica'},
    {'country': 'Jamaica', 'gold': 4},
    {'country': 'Jamaica', 'gold': 4, 'silver': 1},
    {'country': 'Jamaica', 'gold': 4, 'silver': 1, 'bronze': 4},
    {'country': 'Jamaica', 'gold': 4, 'silver': 1, 'bronze': 4, 'rank': 21},
]

    {'country': 'Spain'},
    {'country': 'Spain', 'gold': 3},
    {'country': 'Spain', 'gold': 3, 'silver': 8},
    {'country': 'Spain', 'gold': 3, 'silver': 8, 'bronze': 6},
    {'country': 'Spain', 'gold': 3, 'silver': 8, 'bronze': 6, 'rank': 22},
]

    {'country': 'Sweden'},
    {'country': 'Sweden', 'gold': 3},
    {'country': 'Sweden', 'gold': 3, 'silver': 6},
    {'country': 'Sweden', 'gold': 3, 'silver': 6, 'bronze': 0},
    {'country': 'Sweden', 'gold': 3, 'silver': 6, 'bronze': 0, 'rank': 23},
]

    {'country': 'Switzerland'},
    {'country': 'Switzerland', 'gold': 3},
    {'country': 'Switzerland', 'gold': 3, 'silver': 4},
    {'country': 'Switzerland', 'gold': 3, 'silver': 4, 'bronze': 6},
    {'country': 'Switzerland', 'gold': 3, 'silver': 4, 'bronze': 6, 'rank': 24},
]

    {'country': 'Denmark'},
    {'country': 'Denmark', 'gold': 3},
    {'country': 'Denmark', 'gold': 3, 'silver': 4},
    {'country': 'Denmark', 'gold': 3, 'silver': 4, 'bronze': 4},
    {'country': 'Denmark', 'gold': 3, 'silver': 4, 'bronze': 4, 'rank': 25},
]

    {'country': 'Croatia'},
    {'country': 'Croatia', 'gold': 3},
    {'country': 'Croatia', 'gold': 3, 'silver': 3},
    {'country': 'Croatia', 'gold': 3, 'silver': 3, 'bronze': 2},
    {'country': 'Croatia', 'gold': 3, 'silver': 3, 'bronze': 2, 'rank': 26},
]

    {'country': 'Iran'},
    {'country': 'Iran', 'gold': 3},
    {'country': 'Iran', 'gold': 3, 'silver': 2},
    {'country': 'Iran', 'gold': 3, 'silver': 2, 'bronze': 2},
    {'country': 'Iran', 'gold': 3, 'silver': 2, 'bronze': 2, 'rank': 27},
]

    {'country': 'Serbia'},
    {'country': 'Serbia', 'gold': 3},
    {'country': 'Serbia', 'gold': 3, 'silver': 1},
    {'country': 'Serbia', 'gold': 3, 'silver': 1, 'bronze': 5},
    {'country': 'Serbia', 'gold': 3, 'silver': 1, 'bronze': 5, 'rank': 28},
]

    {'country': 'Belgium'},
    {'country': 'Belgium', 'gold': 3},
    {'country': 'Belgium', 'gold': 3, 'silver': 1},
    {'country': 'Belgium', 'gold': 3, 'silver': 1, 'bronze': 3},
    {'country': 'Belgium', 'gold': 3, 'silver': 1, 'bronze': 3, 'rank': 29},
]

    {'country': 'Bulgaria'},
    {'country': 'Bulgaria', 'gold': 3},
    {'country': 'Bulgaria', 'gold': 3, 'silver': 1},
    {'country': 'Bulgaria', 'gold': 3, 'silver': 1, 'bronze': 2},
    {'country': 'Bulgaria', 'gold': 3, 'silver': 1, 'bronze': 2, 'rank': 30},
]

    {'country': 'Slovenia'},
    {'country': 'Slovenia', 'gold': 3},
    {'country': 'Slovenia', 'gold': 3, 'silver': 1},
    {'country': 'Slovenia', 'gold': 3, 'silver': 1, 'bronze': 1},
    {'country': 'Slovenia', 'gold': 3, 'silver': 1, 'bronze': 1, 'rank': 31},
]

    {'country': 'Uzbekistan'},
    {'country': 'Uzbekistan', 'gold': 3},
    {'country': 'Uzbekistan', 'gold': 3, 'silver': 0},
    {'country': 'Uzbekistan', 'gold': 3, 'silver': 0, 'bronze': 2},
    {'country': 'Uzbekistan', 'gold': 3, 'silver': 0, 'bronze': 2, 'rank': 32},
]

    {'country': 'Georgia'},
    {'country': 'Georgia', 'gold': 2},
    {'country': 'Georgia', 'gold': 2, 'silver': 5},
    {'country': 'Georgia', 'gold': 2, 'silver': 5, 'bronze': 1},
    {'country': 'Georgia', 'gold': 2, 'silver': 5, 'bronze': 1, 'rank': 33},
]

    {'country': 'Chinese Taipei'},
    {'country': 'Chinese Taipei', 'gold': 2},
    {'country': 'Chinese Taipei', 'gold': 2, 'silver': 4},
    {'country': 'Chinese Taipei', 'gold': 2, 'silver': 4, 'bronze': 6},
    {'country': 'Chinese Taipei', 'gold': 2, 'silver': 4, 'bronze': 6, 'rank': 34},
]

    {'country': 'Turkey'},
    {'country': 'Turkey', 'gold': 2},
    {'country': 'Turkey', 'gold': 2, 'silver': 2},
    {'country': 'Turkey', 'gold': 2, 'silver': 2, 'bronze': 9},
    {'country': 'Turkey', 'gold': 2, 'silver': 2, 'bronze': 9, 'rank': 35},
]

    {'country': 'Greece'},
    {'country': 'Greece', 'gold': 2},
    {'country': 'Greece', 'gold': 2, 'silver': 1},
    {'country': 'Greece', 'gold': 2, 'silver': 1, 'bronze': 1},
    {'country': 'Greece', 'gold': 2, 'silver': 1, 'bronze': 1, 'rank': 36},
]

    {'country': 'Uganda'},
    {'country': 'Uganda', 'gold': 2},
    {'country': 'Uganda', 'gold': 2, 'silver': 1},
    {'country': 'Uganda', 'gold': 2, 'silver': 1, 'bronze': 1},
    {'country': 'Uganda', 'gold': 2, 'silver': 1, 'bronze': 1, 'rank': 36},
]

    {'country': 'Ecuador'},
    {'country': 'Ecuador', 'gold': 2},
    {'country': 'Ecuador', 'gold': 2, 'silver': 1},
    {'country': 'Ecuador', 'gold': 2, 'silver': 1, 'bronze': 0},
    {'country': 'Ecuador', 'gold': 2, 'silver': 1, 'bronze': 0, 'rank': 38},
]

    {'country': 'Ireland'},
    {'country': 'Ireland', 'gold': 2},
    {'country': 'Ireland', 'gold': 2, 'silver': 0},
    {'country': 'Ireland', 'gold': 2, 'silver': 0, 'bronze': 2},
    {'country': 'Ireland', 'gold': 2, 'silver': 0, 'bronze': 2, 'rank': 39},
]

    {'country': 'Israel'},
    {'country': 'Israel', 'gold': 2},
    {'country': 'Israel', 'gold': 2, 'silver': 0},
    {'country': 'Israel', 'gold': 2, 'silver': 0, 'bronze': 2},
    {'country': 'Israel', 'gold': 2, 'silver': 0, 'bronze': 2, 'rank': 39},
]

    {'country': 'Qatar'},
    {'country': 'Qatar', 'gold': 2},
    {'country': 'Qatar', 'gold': 2, 'silver': 0},
    {'country': 'Qatar', 'gold': 2, 'silver': 0, 'bronze': 1},
    {'country': 'Qatar', 'gold': 2, 'silver': 0, 'bronze': 1, 'rank': 41},
]

    {'country': 'Bahamas'},
    {'country': 'Bahamas', 'gold': 2},
    {'country': 'Bahamas', 'gold': 2, 'silver': 0},
    {'country': 'Bahamas', 'gold': 2, 'silver': 0, 'bronze': 0},
    {'country': 'Bahamas', 'gold': 2, 'silver': 0, 'bronze': 0, 'rank': 42},
]

    {'country': 'Kosovo'},
    {'country': 'Kosovo', 'gold': 2},
    {'country': 'Kosovo', 'gold': 2, 'silver': 0},
    {'country': 'Kosovo', 'gold': 2, 'silver': 0, 'bronze': 0},
    {'country': 'Kosovo', 'gold': 2, 'silver': 0, 'bronze': 0, 'rank': 42},
]

    {'country': 'Ukraine'},
    {'country': 'Ukraine', 'gold': 1},
    {'country': 'Ukraine', 'gold': 1, 'silver': 6},
    {'country': 'Ukraine', 'gold': 1, 'silver': 6, 'bronze': 12},
    {'country': 'Ukraine', 'gold': 1, 'silver': 6, 'bronze': 12, 'rank': 44},
]

    {'country': 'Belarus'},
    {'country': 'Belarus', 'gold': 1},
    {'country': 'Belarus', 'gold': 1, 'silver': 3},
    {'country': 'Belarus', 'gold': 1, 'silver': 3, 'bronze': 3},
    {'country': 'Belarus', 'gold': 1, 'silver': 3, 'bronze': 3, 'rank': 45},
]

    {'country': 'Romania'},
    {'country': 'Romania', 'gold': 1},
    {'country': 'Romania', 'gold': 1, 'silver': 3},
    {'country': 'Romania', 'gold': 1, 'silver': 3, 'bronze': 0},
    {'country': 'Romania', 'gold': 1, 'silver': 3, 'bronze': 0, 'rank': 46},
]

    {'country': 'Venezuela'},
    {'country': 'Venezuela', 'gold': 1},
    {'country': 'Venezuela', 'gold': 1, 'silver': 3},
    {'country': 'Venezuela', 'gold': 1, 'silver': 3, 'bronze': 0},
    {'country': 'Venezuela', 'gold': 1, 'silver': 3, 'bronze': 0, 'rank': 46},
]

    {'country': 'India'},
    {'country': 'India', 'gold': 1},
    {'country': 'India', 'gold': 1, 'silver': 2},
    {'country': 'India', 'gold': 1, 'silver': 2, 'bronze': 4},
    {'country': 'India', 'gold': 1, 'silver': 2, 'bronze': 4, 'rank': 48},
]

    {'country': 'Hong Kong'},
    {'country': 'Hong Kong', 'gold': 1},
    {'country': 'Hong Kong', 'gold': 1, 'silver': 2},
    {'country': 'Hong Kong', 'gold': 1, 'silver': 2, 'bronze': 3},
    {'country': 'Hong Kong', 'gold': 1, 'silver': 2, 'bronze': 3, 'rank': 49},
]

    {'country': 'Philippines'},
    {'country': 'Philippines', 'gold': 1},
    {'country': 'Philippines', 'gold': 1, 'silver': 2},
    {'country': 'Philippines', 'gold': 1, 'silver': 2, 'bronze': 1},
    {'country': 'Philippines', 'gold': 1, 'silver': 2, 'bronze': 1, 'rank': 50},
]

    {'country': 'Slovakia'},
    {'country': 'Slovakia', 'gold': 1},
    {'country': 'Slovakia', 'gold': 1, 'silver': 2},
    {'country': 'Slovakia', 'gold': 1, 'silver': 2, 'bronze': 1},
    {'country': 'Slovakia', 'gold': 1, 'silver': 2, 'bronze': 1, 'rank': 50},
]

    {'country': 'South Africa'},
    {'country': 'South Africa', 'gold': 1},
    {'country': 'South Africa', 'gold': 1, 'silver': 2},
    {'country': 'South Africa', 'gold': 1, 'silver': 2, 'bronze': 0},
    {'country': 'South Africa', 'gold': 1, 'silver': 2, 'bronze': 0, 'rank': 52},
]

    {'country': 'Austria'},
    {'country': 'Austria', 'gold': 1},
    {'country': 'Austria', 'gold': 1, 'silver': 1},
    {'country': 'Austria', 'gold': 1, 'silver': 1, 'bronze': 5},
    {'country': 'Austria', 'gold': 1, 'silver': 1, 'bronze': 5, 'rank': 53},
]

    {'country': 'Egypt'},
    {'country': 'Egypt', 'gold': 1},
    {'country': 'Egypt', 'gold': 1, 'silver': 1},
    {'country': 'Egypt', 'gold': 1, 'silver': 1, 'bronze': 4},
    {'country': 'Egypt', 'gold': 1, 'silver': 1, 'bronze': 4, 'rank': 54},
]

    {'country': 'Indonesia'},
    {'country': 'Indonesia', 'gold': 1},
    {'country': 'Indonesia', 'gold': 1, 'silver': 1},
    {'country': 'Indonesia', 'gold': 1, 'silver': 1, 'bronze': 3},
    {'country': 'Indonesia', 'gold': 1, 'silver': 1, 'bronze': 3, 'rank': 55},
]

    {'country': 'Ethiopia'},
    {'country': 'Ethiopia', 'gold': 1},
    {'country': 'Ethiopia', 'gold': 1, 'silver': 1},
    {'country': 'Ethiopia', 'gold': 1, 'silver': 1, 'bronze': 2},
    {'country': 'Ethiopia', 'gold': 1, 'silver': 1, 'bronze': 2, 'rank': 56},
]

    {'country': 'Portugal'},
    {'country': 'Portugal', 'gold': 1},
    {'country': 'Portugal', 'gold': 1, 'silver': 1},
    {'country': 'Portugal', 'gold': 1, 'silver': 1, 'bronze': 2},
    {'country': 'Portugal', 'gold': 1, 'silver': 1, 'bronze': 2, 'rank': 56},
]

    {'country': 'Tunisia'},
    {'country': 'Tunisia', 'gold': 1},
    {'country': 'Tunisia', 'gold': 1, 'silver': 1},
    {'country': 'Tunisia', 'gold': 1, 'silver': 1, 'bronze': 0},
    {'country': 'Tunisia', 'gold': 1, 'silver': 1, 'bronze': 0, 'rank': 58},
]

    {'country': 'Estonia'},
    {'country': 'Estonia', 'gold': 1},
    {'country': 'Estonia', 'gold': 1, 'silver': 0},
    {'country': 'Estonia', 'gold': 1, 'silver': 0, 'bronze': 1},
    {'country': 'Estonia', 'gold': 1, 'silver': 0, 'bronze': 1, 'rank': 59},
]

    {'country': 'Fiji'},
    {'country': 'Fiji', 'gold': 1},
    {'country': 'Fiji', 'gold': 1, 'silver': 0},
    {'country': 'Fiji', 'gold': 1, 'silver': 0, 'bronze': 1},
    {'country': 'Fiji', 'gold': 1, 'silver': 0, 'bronze': 1, 'rank': 59},
]

    {'country': 'Latvia'},
    {'country': 'Latvia', 'gold': 1},
    {'country': 'Latvia', 'gold': 1, 'silver': 0},
    {'country': 'Latvia', 'gold': 1, 'silver': 0, 'bronze': 1},
    {'country': 'Latvia', 'gold': 1, 'silver': 0, 'bronze': 1, 'rank': 59},
]

    {'country': 'Thailand'},
    {'country': 'Thailand', 'gold': 1},
    {'country': 'Thailand', 'gold': 1, 'silver': 0},
    {'country': 'Thailand', 'gold': 1, 'silver': 0, 'bronze': 1},
    {'country': 'Thailand', 'gold': 1, 'silver': 0, 'bronze': 1, 'rank': 59},
]

    {'country': 'Bermuda'},
    {'country': 'Bermuda', 'gold': 1},
    {'country': 'Bermuda', 'gold': 1, 'silver': 0},
    {'country': 'Bermuda', 'gold': 1, 'silver': 0, 'bronze': 0},
    {'country': 'Bermuda', 'gold': 1, 'silver': 0, 'bronze': 0, 'rank': 63},
]

    {'country': 'Morocco'},
    {'country': 'Morocco', 'gold': 1},
    {'country': 'Morocco', 'gold': 1, 'silver': 0},
    {'country': 'Morocco', 'gold': 1, 'silver': 0, 'bronze': 0},
    {'country': 'Morocco', 'gold': 1, 'silver': 0, 'bronze': 0, 'rank': 63},
]

    {'country': 'Puerto Rico'},
    {'country': 'Puerto Rico', 'gold': 1},
    {'country': 'Puerto Rico', 'gold': 1, 'silver': 0},
    {'country': 'Puerto Rico', 'gold': 1, 'silver': 0, 'bronze': 0},
    {'country': 'Puerto Rico', 'gold': 1, 'silver': 0, 'bronze': 0, 'rank': 63},
]

    {'country': 'Colombia'},
    {'country': 'Colombia', 'gold': 0},
    {'country': 'Colombia', 'gold': 0, 'silver': 4},
    {'country': 'Colombia', 'gold': 0, 'silver': 4, 'bronze': 1},
    {'country': 'Colombia', 'gold': 0, 'silver': 4, 'bronze': 1, 'rank': 66},
]

    {'country': 'Azerbaijan'},
    {'country': 'Azerbaijan', 'gold': 0},
    {'country': 'Azerbaijan', 'gold': 0, 'silver': 3},
    {'country': 'Azerbaijan', 'gold': 0, 'silver': 3, 'bronze': 4},
    {'country': 'Azerbaijan', 'gold': 0, 'silver': 3, 'bronze': 4, 'rank': 67},
]

    {'country': 'Dominican Republic'},
    {'country': 'Dominican Republic', 'gold': 0},
    {'country': 'Dominican Republic', 'gold': 0, 'silver': 3},
    {'country': 'Dominican Republic', 'gold': 0, 'silver': 3, 'bronze': 2},
    {'country': 'Dominican Republic', 'gold': 0,
        'silver': 3, 'bronze': 2, 'rank': 68},
]

    {'country': 'Armenia'},
    {'country': 'Armenia', 'gold': 0},
    {'country': 'Armenia', 'gold': 0, 'silver': 2},
    {'country': 'Armenia', 'gold': 0, 'silver': 2, 'bronze': 2},
    {'country': 'Armenia', 'gold': 0, 'silver': 2, 'bronze': 2, 'rank': 69},
]

    {'country': 'Kyrgyzstan'},
    {'country': 'Kyrgyzstan', 'gold': 0},
    {'country': 'Kyrgyzstan', 'gold': 0, 'silver': 2},
    {'country': 'Kyrgyzstan', 'gold': 0, 'silver': 2, 'bronze': 1},
    {'country': 'Kyrgyzstan', 'gold': 0, 'silver': 2, 'bronze': 1, 'rank': 70},
]

    {'country': 'Mongolia'},
    {'country': 'Mongolia', 'gold': 0},
    {'country': 'Mongolia', 'gold': 0, 'silver': 1},
    {'country': 'Mongolia', 'gold': 0, 'silver': 1, 'bronze': 3},
    {'country': 'Mongolia', 'gold': 0, 'silver': 1, 'bronze': 3, 'rank': 71},
]

    {'country': 'Argentina'},
    {'country': 'Argentina', 'gold': 0},
    {'country': 'Argentina', 'gold': 0, 'silver': 1},
    {'country': 'Argentina', 'gold': 0, 'silver': 1, 'bronze': 2},
    {'country': 'Argentina', 'gold': 0, 'silver': 1, 'bronze': 2, 'rank': 72},
]

    {'country': 'San Marino'},
    {'country': 'San Marino', 'gold': 0},
    {'country': 'San Marino', 'gold': 0, 'silver': 1},
    {'country': 'San Marino', 'gold': 0, 'silver': 1, 'bronze': 2},
    {'country': 'San Marino', 'gold': 0, 'silver': 1, 'bronze': 2, 'rank': 72},
]

    {'country': 'Jordan'},
    {'country': 'Jordan', 'gold': 0},
    {'country': 'Jordan', 'gold': 0, 'silver': 1},
    {'country': 'Jordan', 'gold': 0, 'silver': 1, 'bronze': 1},
    {'country': 'Jordan', 'gold': 0, 'silver': 1, 'bronze': 1, 'rank': 74},
]

    {'country': 'Malaysia'},
    {'country': 'Malaysia', 'gold': 0},
    {'country': 'Malaysia', 'gold': 0, 'silver': 1},
    {'country': 'Malaysia', 'gold': 0, 'silver': 1, 'bronze': 1},
    {'country': 'Malaysia', 'gold': 0, 'silver': 1, 'bronze': 1, 'rank': 74},
]

    {'country': 'Nigeria'},
    {'country': 'Nigeria', 'gold': 0},
    {'country': 'Nigeria', 'gold': 0, 'silver': 1},
    {'country': 'Nigeria', 'gold': 0, 'silver': 1, 'bronze': 1},
    {'country': 'Nigeria', 'gold': 0, 'silver': 1, 'bronze': 1, 'rank': 74},
]

    {'country': 'Bahrain'},
    {'country': 'Bahrain', 'gold': 0},
    {'country': 'Bahrain', 'gold': 0, 'silver': 1},
    {'country': 'Bahrain', 'gold': 0, 'silver': 1, 'bronze': 0},
    {'country': 'Bahrain', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
]

    {'country': 'Saudi Arabia'},
    {'country': 'Saudi Arabia', 'gold': 0},
    {'country': 'Saudi Arabia', 'gold': 0, 'silver': 1},
    {'country': 'Saudi Arabia', 'gold': 0, 'silver': 1, 'bronze': 0},
    {'country': 'Saudi Arabia', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
]

    {'country': 'Lithuania'},
    {'country': 'Lithuania', 'gold': 0},
    {'country': 'Lithuania', 'gold': 0, 'silver': 1},
    {'country': 'Lithuania', 'gold': 0, 'silver': 1, 'bronze': 0},
    {'country': 'Lithuania', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
]

    {'country': 'North Macedonia'},
    {'country': 'North Macedonia', 'gold': 0},
    {'country': 'North Macedonia', 'gold': 0, 'silver': 1},
    {'country': 'North Macedonia', 'gold': 0, 'silver': 1, 'bronze': 0},
    {'country': 'North Macedonia', 'gold': 0,
        'silver': 1, 'bronze': 0, 'rank': 77},
]

    {'country': 'Namibia'},
    {'country': 'Namibia', 'gold': 0},
    {'country': 'Namibia', 'gold': 0, 'silver': 1},
    {'country': 'Namibia', 'gold': 0, 'silver': 1, 'bronze': 0},
    {'country': 'Namibia', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
]

    {'country': 'Turkmenistan'},
    {'country': 'Turkmenistan', 'gold': 0},
    {'country': 'Turkmenistan', 'gold': 0, 'silver': 1},
    {'country': 'Turkmenistan', 'gold': 0, 'silver': 1, 'bronze': 0},
    {'country': 'Turkmenistan', 'gold': 0, 'silver': 1, 'bronze': 0, 'rank': 77},
]

    {'country': 'Kazakhstan'},
    {'country': 'Kazakhstan', 'gold': 0},
    {'country': 'Kazakhstan', 'gold': 0, 'silver': 0},
    {'country': 'Kazakhstan', 'gold': 0, 'silver': 0, 'bronze': 8},
    {'country': 'Kazakhstan', 'gold': 0, 'silver': 0, 'bronze': 8, 'rank': 83},
]

    {'country': 'Mexico'},
    {'country': 'Mexico', 'gold': 0},
    {'country': 'Mexico', 'gold': 0, 'silver': 0},
    {'country': 'Mexico', 'gold': 0, 'silver': 0, 'bronze': 4},
    {'country': 'Mexico', 'gold': 0, 'silver': 0, 'bronze': 4, 'rank': 84},
]

    {'country': 'Finland'},
    {'country': 'Finland', 'gold': 0},
    {'country': 'Finland', 'gold': 0, 'silver': 0},
    {'country': 'Finland', 'gold': 0, 'silver': 0, 'bronze': 2},
    {'country': 'Finland', 'gold': 0, 'silver': 0, 'bronze': 2, 'rank': 85},
]

    {'country': 'Botswana'},
    {'country': 'Botswana', 'gold': 0},
    {'country': 'Botswana', 'gold': 0, 'silver': 0},
    {'country': 'Botswana', 'gold': 0, 'silver': 0, 'bronze': 1},
    {'country': 'Botswana', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
]

    {'country': 'Burkina Faso'},
    {'country': 'Burkina Faso', 'gold': 0},
    {'country': 'Burkina Faso', 'gold': 0, 'silver': 0},
    {'country': 'Burkina Faso', 'gold': 0, 'silver': 0, 'bronze': 1},
    {'country': 'Burkina Faso', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
]

    {'country': "Côte d'Ivoire"},
    {'country': "Côte d'Ivoire", 'gold': 0},
    {'country': "Côte d'Ivoire", 'gold': 0, 'silver': 0},
    {'country': "Côte d'Ivoire", 'gold': 0, 'silver': 0, 'bronze': 1},
    {'country': "Côte d'Ivoire", 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
]

    {'country': 'Ghana'},
    {'country': 'Ghana', 'gold': 0},
    {'country': 'Ghana', 'gold': 0, 'silver': 0},
    {'country': 'Ghana', 'gold': 0, 'silver': 0, 'bronze': 1},
    {'country': 'Ghana', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
]

    {'country': 'Grenada'},
    {'country': 'Grenada', 'gold': 0},
    {'country': 'Grenada', 'gold': 0, 'silver': 0},
    {'country': 'Grenada', 'gold': 0, 'silver': 0, 'bronze': 1},
    {'country': 'Grenada', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
]

    {'country': 'Kuwait'},
    {'country': 'Kuwait', 'gold': 0},
    {'country': 'Kuwait', 'gold': 0, 'silver': 0},
    {'country': 'Kuwait', 'gold': 0, 'silver': 0, 'bronze': 1},
    {'country': 'Kuwait', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
]

    {'country': 'Moldova'},
    {'country': 'Moldova', 'gold': 0},
    {'country': 'Moldova', 'gold': 0, 'silver': 0},
    {'country': 'Moldova', 'gold': 0, 'silver': 0, 'bronze': 1},
    {'country': 'Moldova', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
]

    {'country': 'Syria'},
    {'country': 'Syria', 'gold': 0},
    {'country': 'Syria', 'gold': 0, 'silver': 0},
    {'country': 'Syria', 'gold': 0, 'silver': 0, 'bronze': 1},
    {'country': 'Syria', 'gold': 0, 'silver': 0, 'bronze': 1, 'rank': 86},
]
