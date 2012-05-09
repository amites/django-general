# coding: utf-8

#
# Generic Lists of Choices
#

STATE_CHOICES = (
    ('', '-- Select --'),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'Washington, DC'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania '),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
    ('XX', 'Other'),
)

US_STATES_LATLON = (
#Geographic center of US
    ('', '39.50,98.35'),
    ('AK', '61.3850,-152.2683'),
    ('AL', '32.7990,-86.8073'),
    ('AR', '34.9513,-92.3809'),
    ('AS', '14.2417,-170.7197'),
    ('AZ', '33.7712,-111.3877'),
    ('CA', '36.1700,-119.7462'),
    ('CO', '39.0646,-105.3272'),
    ('CT', '41.5834,-72.7622'),
    ('DC', '38.8964,-77.0262'),
    ('DE', '39.3498,-75.5148'),
    ('FL', '27.8333,-81.7170'),
    ('GA', '32.9866,-83.6487'),
    ('HI', '21.1098,-157.5311'),
    ('IA', '42.0046,-93.2140'),
    ('ID', '44.2394,-114.5103'),
    ('IL', '40.3363,-89.0022'),
    ('IN', '39.8647,-86.2604'),
    ('KS', '38.5111,-96.8005'),
    ('KY', '37.6690,-84.6514'),
    ('LA', '31.1801,-91.8749'),
    ('MA', '42.2373,-71.5314'),
    ('MD', '39.0724,-76.7902'),
    ('ME', '44.6074,-69.3977'),
    ('MI', '43.3504,-84.5603'),
    ('MN', '45.7326,-93.9196'),
    ('MO', '38.4623,-92.3020'),
    ('MP', '14.8058,145.5505'),
    ('MS', '32.7673,-89.6812'),
    ('MT', '46.9048,-110.3261'),
    ('NC', '35.6411,-79.8431'),
    ('ND', '47.5362,-99.7930'),
    ('NE', '41.1289,-98.2883'),
    ('NH', '43.4108,-71.5653'),
    ('NJ', '40.3140,-74.5089'),
    ('NM', '34.8375,-106.2371'),
    ('NV', '38.4199,-117.1219'),
    ('NY', '42.1497,-74.9384'),
    ('OH', '40.3736,-82.7755'),
    ('OK', '35.5376,-96.9247'),
    ('OR', '44.5672,-122.1269'),
    ('PA', '40.5773,-77.2640'),
    ('PR', '18.2766,-66.3350'),
    ('RI', '41.6772,-71.5101'),
    ('SC', '33.8191,-80.9066'),
    ('SD', '44.2853,-99.4632'),
    ('TN', '35.7449,-86.7489'),
    ('TX', '31.1060,-97.6475'),
    ('UT', '40.1135,-111.8535'),
    ('VA', '37.7680,-78.2057'),
    ('VI', '18.0001,-64.8199'),
    ('VT', '44.0407,-72.7093'),
    ('WA', '47.3917,-121.5708'),
    ('WI', '44.2563,-89.6385'),
    ('WV', '38.4680,-80.9696'),
    ('WY', '42.7475,-107.2085'),
#Geographic center of US
    ('XX', '39.50,98.35'),
)

# October 2009 - from Gmail sign-up
COUNTRY_CHOICES = (
    ('', '---SELECT---'),
    ('AF', 'Afghanistan'),
    ('AX', 'Aland Islands'),
    ('AL', 'Albania'),

    ('DZ', 'Algeria'),
    ('AS', 'American Samoa'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AI', 'Anguilla'),
    ('AQ', 'Antarctica'),
    ('AG', 'Antigua and Barbuda'),

    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AW', 'Aruba'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'),

    ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Belarus'),
    ('BE', 'Belgium'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),

    ('BM', 'Bermuda'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivia'),
    ('BA', 'Bosnia and Herzegovina'),
    ('BW', 'Botswana'),
    ('BV', 'Bouvet Island'),
    ('BR', 'Brazil'),

    ('IO', 'British Indian Ocean Territory'),
    ('BN', 'Brunei'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('KH', 'Cambodia'),
    ('CM', 'Cameroon'),

    ('CA', 'Canada'),
    ('CV', 'Cape Verde'),
    ('KY', 'Cayman Islands'),
    ('CF', 'Central African Republic'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),

    ('CX', 'Christmas Island'),
    ('CC', 'Cocos Islands'),
    ('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CG', 'Congo'),
    ('CD', 'Congo, Democratic Republic of the'),
    ('CK', 'Cook Islands'),

    ('CR', 'Costa Rica'),
    ('CI', 'Côte d&#39;Ivoire'),
    ('HR', 'Croatia'),
    ('CU', 'Cuba'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DK', 'Denmark'),

    ('DJ', 'Djibouti'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('EC', 'Ecuador'),
    ('EG', 'Egypt'),
    ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'),

    ('ER', 'Eritrea'),
    ('EE', 'Estonia'),
    ('ET', 'Ethiopia'),
    ('FK', 'Falkland Islands'),
    ('FO', 'Faroe Islands'),
    ('FJ', 'Fiji'),
    ('FI', 'Finland'),

    ('FR', 'France'),
    ('GF', 'French Guiana'),
    ('PF', 'French Polynesia'),
    ('TF', 'French Southern Territories'),
    ('GA', 'Gabon'),
    ('GM', 'Gambia'),
    ('GE', 'Georgia'),

    ('DE', 'Germany'),
    ('GH', 'Ghana'),
    ('GI', 'Gibraltar'),
    ('GR', 'Greece'),
    ('GL', 'Greenland'),
    ('GD', 'Grenada'),
    ('GP', 'Guadeloupe'),

    ('GU', 'Guam'),
    ('GT', 'Guatemala'),
    ('GG', 'Guernsey'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-Bissau'),
    ('GY', 'Guyana'),
    ('HT', 'Haiti'),

    ('HM', 'Heard Island and McDonald Islands'),
    ('HN', 'Honduras'),
    ('HK', 'Hong Kong'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),

    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IM', 'Isle of Man'),
    ('IL', 'Israel'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),

    ('JP', 'Japan'),
    ('JE', 'Jersey'),
    ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'),
    ('KI', 'Kiribati'),
    ('KW', 'Kuwait'),

    ('KG', 'Kyrgyzstan'),
    ('LA', 'Laos'),
    ('LV', 'Latvia'),
    ('LB', 'Lebanon'),
    ('LS', 'Lesotho'),
    ('LR', 'Liberia'),
    ('LY', 'Libya'),

    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('MO', 'Macao'),
    ('MK', 'Macedonia'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),

    ('MY', 'Malaysia'),
    ('MV', 'Maldives'),
    ('ML', 'Mali'),
    ('MT', 'Malta'),
    ('MH', 'Marshall Islands'),
    ('MQ', 'Martinique'),
    ('MR', 'Mauritania'),

    ('MU', 'Mauritius'),
    ('YT', 'Mayotte'),
    ('MX', 'Mexico'),
    ('FM', 'Micronesia'),
    ('MD', 'Moldova'),
    ('MC', 'Monaco'),
    ('MN', 'Mongolia'),

    ('ME', 'Montenegro'),
    ('MS', 'Montserrat'),
    ('MA', 'Morocco'),
    ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),

    ('NP', 'Nepal'),
    ('NL', 'Netherlands'),
    ('AN', 'Netherlands Antilles'),
    ('NC', 'New Caledonia'),
    ('NZ', 'New Zealand'),
    ('NI', 'Nicaragua'),
    ('NE', 'Niger'),

    ('NG', 'Nigeria'),
    ('NU', 'Niue'),
    ('NF', 'Norfolk Island'),
    ('MP', 'Northern Mariana Islands'),
    ('KP', 'North Korea'),
    ('NO', 'Norway'),
    ('OM', 'Oman'),

    ('PK', 'Pakistan'),
    ('PW', 'Palau'),
    ('PS', 'Palestinian Territories'),
    ('PA', 'Panama'),
    ('PG', 'Papua New Guinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Peru'),

    ('PH', 'Philippines'),
    ('PN', 'Pitcairn'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('PR', 'Puerto Rico'),
    ('QA', 'Qatar'),
    ('RE', 'Reunion'),

    ('RO', 'Romania'),
    ('RU', 'Russia'),
    ('RW', 'Rwanda'),
    ('SH', 'Saint Helena'),
    ('KN', 'Saint Kitts and Nevis'),
    ('LC', 'Saint Lucia'),
    ('PM', 'Saint Pierre and Miquelon'),

    ('VC', 'Saint Vincent and the Grenadines'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'São Tomé and Príncipe'),
    ('SA', 'Saudi Arabia'),
    ('SN', 'Senegal'),
    ('RS', 'Serbia'),

    ('CS', 'Serbia and Montenegro'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leone'),
    ('SG', 'Singapore'),
    ('SK', 'Slovakia'),
    ('SI', 'Slovenia'),
    ('SB', 'Solomon Islands'),

    ('SO', 'Somalia'),
    ('ZA', 'South Africa'),
    ('GS', 'South Georgia and the South Sandwich Islands'),
    ('KR', 'South Korea'),
    ('ES', 'Spain'),
    ('LK', 'Sri Lanka'),
    ('SD', 'Sudan'),

    ('SR', 'Suriname'),
    ('SJ', 'Svalbard and Jan Mayen'),
    ('SZ', 'Swaziland'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('SY', 'Syria'),
    ('TW', 'Taiwan'),

    ('TJ', 'Tajikistan'),
    ('TZ', 'Tanzania'),
    ('TH', 'Thailand'),
    ('TL', 'Timor-Leste'),
    ('TG', 'Togo'),
    ('TK', 'Tokelau'),
    ('TO', 'Tonga'),

    ('TT', 'Trinidad and Tobago'),
    ('TN', 'Tunisia'),
    ('TR', 'Turkey'),
    ('TM', 'Turkmenistan'),
    ('TC', 'Turks and Caicos Islands'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),

    ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'),
    ('GB', 'United Kingdom'),
    ('US', 'United States'),
    ('UM', 'United States minor outlying islands'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),

    ('VU', 'Vanuatu'),
    ('VA', 'Vatican City'),
    ('VE', 'Venezuela'),
    ('VN', 'Vietnam'),
    ('VG', 'Virgin Islands, British'),
    ('VI', 'Virgin Islands, U.S.'),
    ('WF', 'Wallis and Futuna'),

    ('EH', 'Western Sahara'),
    ('YE', 'Yemen'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabwe'),
)
