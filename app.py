from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "b5bbb7f8fae9d8f3e5c4a4d50641eb21"

# Language code to full name mapping
LANGUAGE_MAPPING = {
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'zh': 'Chinese',
    'ar': 'Arabic',
    'ru': 'Russian',
    'pt': 'Portuguese',
    'nl': 'Dutch',
    'hi': 'Hindi',
    'tr': 'Turkish',
    'th': 'Thai',
    'vi': 'Vietnamese',
    'sv': 'Swedish',
    'da': 'Danish',
    'fi': 'Finnish',
    'no': 'Norwegian',
    'pl': 'Polish',
    'hu': 'Hungarian',
    'cs': 'Czech',
    'el': 'Greek',
    'ro': 'Romanian',
    'id': 'Indonesian',
    'he': 'Hebrew',
    'sk': 'Slovak',
    'sr': 'Serbian',
    'uk': 'Ukrainian',
    'bg': 'Bulgarian',
    'hr': 'Croatian',
    'lt': 'Lithuanian',
    'sl': 'Slovenian',
    'et': 'Estonian',
    'lv': 'Latvian',
    'fa': 'Persian',
    'ms': 'Malay',
    'ta': 'Tamil',
    'bn': 'Bengali',
    'kn': 'Kannada',
    'te': 'Telugu',
    'mr': 'Marathi',
    'gu': 'Gujarati',
    'ur': 'Urdu',
    'th': 'Thai',
    'mn': 'Mongolian',
    'my': 'Burmese',
    'ka': 'Georgian',
    'sw': 'Swahili',
    'am': 'Amharic',
    'zu': 'Zulu',
    'xh': 'Xhosa',
    'af': 'Afrikaans',
    'sq': 'Albanian',
    'cy': 'Welsh',
    'is': 'Icelandic',
    'mt': 'Maltese',
    'lb': 'Luxembourgish',
    'eu': 'Basque',
    'gl': 'Galician',
    'bs': 'Bosnian',
    'fy': 'Frisian',
    'fo': 'Faroese',
    'gd': 'Scottish Gaelic',
    'ga': 'Irish',
    'sm': 'Samoan',
    'to': 'Tongan',
    'haw': 'Hawaiian',
    'mi': 'Maori',
    'sm': 'Samoan',
    'tpi': 'Tok Pisin',
    'tk': 'Turkmen',
    'kl': 'Greenlandic',
    'iu': 'Inuktitut',
    'yo': 'Yoruba',
    'ha': 'Hausa',
    'ig': 'Igbo',
    'sn': 'Shona',
    'st': 'Southern Sotho',
    'nso': 'Northern Sotho',
    'tn': 'Tswana',
    'ts': 'Tsonga',
    've': 'Venda',
    'xh': 'Xhosa',
    'zu': 'Zulu',
    'si': 'Sinhala',
    'dv': 'Divehi',
    'dz': 'Dzongkha',
    'ne': 'Nepali',
    'pa': 'Punjabi',
    'gu': 'Gujarati',
    'as': 'Assamese',
    'or': 'Odia',
    'ml': 'Malayalam',
    'kok': 'Konkani',
    'mni': 'Manipuri',
    'kok': 'Konkani',
    'sd': 'Sindhi',
    'ks': 'Kashmiri',
    'doi': 'Dogri',
    'mai': 'Maithili',
    'ne': 'Nepali',
    'sa': 'Sanskrit',
    'lus': 'Mizo',
    'kha': 'Khasi',
    'gur': 'Frafra',
    'grb': 'Grebo',
    'crh': 'Crimean Tatar',
    'xmf': 'Mingrelian',
    'ady': 'Adyghe',
    'ady': 'Adyghe',
    'kbd': 'Kabardian',
    'lez': 'Lezgian',
    'av': 'Avaric',
    'tuk': 'Turkmen',
    'krc': 'Karachay-Balkar',
    'kum': 'Kumyk',
    'dar': 'Dargwa',
    'ce': 'Chechen',
    'inh': 'Ingush',
    'bxr': 'Russia Buriat',
    'bua': 'Buriat',
    'tyv': 'Tuvinian',
    'alt': 'Southern Altai',
    'sah': 'Yakut',
    'kbd': 'Kabardian',
    'udm': 'Udmurt',
    'mrj': 'Hill Mari',
    'mhr': 'Eastern Mari',
    'chm': 'Mari',
    'koi': 'Komi-Permyak',
    'kpv': 'Komi-Zyrian',
    'sma': 'Southern Sami',
    'sju': 'Ume Sami',
    'smj': 'Lule Sami',
    'se': 'Northern Sami',
    'sms': 'Skolt Sami',
    'sma': 'Southern Sami',
    'sme': 'Northern Sami',
    'szl': 'Silesian',
    'csb': 'Kashubian',
    'ltg': 'Latgalian',
    'glk': 'Gilaki',
    'zza': 'Zaza',
    'kab': 'Kabyle',
    'shi': 'Tachelhit',
    'ary': 'Moroccan Arabic',
    'ary': 'Moroccan Arabic',
    'lrc': 'Northern Luri',
    'luz': 'Southern Luri',
    'pes': 'Western Farsi',
    'ary': 'Moroccan Arabic',
    'ary': 'Moroccan Arabic',
    'ary': 'Moroccan Arabic',
    'shu': 'Chadian Arabic',
    'hau': 'Hausa',
    'ibb': 'Ibibio',
    'bss': 'Akoose',
    'bjn': 'Banjar',
    'arq': 'Algerian Arabic',
    'frp': 'Arpitan',
    'crs': 'Seselwa Creole French',
    'mfe': 'Morisyen',
    'gcf': 'Guadeloupean Creole French',
    'rm': 'Romansh',
    'lmo': 'Lombard',
    'eml': 'Emilian',
    'lij': 'Ligurian',
    'fur': 'Friulian',
    'sc': 'Sardinian',
    'nap': 'Neapolitan',
    'vec': 'Venetian',
    'co': 'Corsican',
    'scn': 'Sicilian',
    'roa': 'Romance languages',
    'la': 'Latin',
    'wa': 'Walloon',
    'gsw': 'Swiss German',
    'bar': 'Bavarian',
    'ksh': 'Colognian',
    'als': 'Alemannic German',
    'pfl': 'Palatine German',
    'dsb': 'Lower Sorbian',
    'hsb': 'Upper Sorbian',
    'fy': 'West Frisian',
    'fy': 'West Frisian',
    'vro': 'Võro',
    'vls': 'West Flemish',
    'nl': 'Dutch Low Saxon',
    'li': 'Limburgish',
    'stq': 'Saterland Frisian',
    'kab': 'Kabyle',
    'tg': 'Tajik',
    'os': 'Ossetic',
    'km': 'Khmer',
    'bpy': 'Bishnupriya Manipuri',
    'ps': 'Pashto',
    'bo': 'Tibetan',
    'dz': 'Dzongkha',
    'chr': 'Cherokee',
    'cr': 'Cree',
    'iu': 'Inuktitut',
    'kl': 'Greenlandic',
    'om': 'Oromo',
    'ti': 'Tigrinya',
    'so': 'Somali',
    'om': 'Oromo',
    'am': 'Amharic',
    'tig': 'Tigre',
    'gn': 'Guarani',
    'qu': 'Quechua',
    'ay': 'Aymara',
    'nah': 'Nahuatl',
    'pap': 'Papiamento',
    'cr': 'Cree',
    'chb': 'Chibcha',
    'war': 'Waray',
    'ceb': 'Cebuano',
    'ilo': 'Ilokano',
    'hil': 'Hiligaynon',
    'jv': 'Javanese',
    'su': 'Sundanese',
    'mg': 'Malagasy',
    'ht': 'Haitian Creole',
    'gv': 'Manx',
    'gv': 'Manx',
    'gag': 'Gagauz',
    'lzh': 'Literary Chinese',
    'sa': 'Sanskrit',
    'doi': 'Dogri',
    'mus': 'Creek',
    'gn': 'Guarani',
    'ay': 'Aymara',
    'rar': 'Rarotongan',
    'tpi': 'Tok Pisin',
    'tpi': 'Tok Pisin',
    'kg': 'Kongo',
    'ny': 'Nyanja',
    'mgh': 'Makhuwa-Meetto',
    'ks': 'Kashmiri',
    'ks': 'Kashmiri',
    'bho': 'Bhojpuri',
    'brh': 'Brahui',
    'bqi': 'Bakhtiari',
    'gbm': 'Garhwali',
    'doi': 'Dogri',
    'sd': 'Sindhi',
    'as': 'Assamese',
    'bh': 'Bihari',
    'doi': 'Dogri',
    'doi': 'Dogri',
    'doi': 'Dogri',
    'doi': 'Dogri',
    'doi': 'Dogri',
    'doi': 'Dogri',
    'doi': 'Dogri',
    'doi': 'Dogri',
    'doi': 'Dogri',
    'doi': 'Dogri',
}



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    movie_name = request.form['movieName']
    recommendations = get_movie_recommendations(movie_name)
    return render_template('recommendations.html', recommendations=recommendations)

def get_movie_recommendations(movie_name):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": API_KEY,
        "query": movie_name
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data['results']:
            movie_id = data['results'][0]['id']
            return fetch_recommendations(movie_id)
        else:
            return []
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

def fetch_recommendations(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"
    params = {"api_key": API_KEY}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        recommendations = []
        for movie in data['results']:
            details = fetch_movie_details(movie['id'])
            recommendations.append(details)
        return recommendations
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return []

def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": API_KEY, "append_to_response": "credits"}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        language_code = data['original_language']
        language = LANGUAGE_MAPPING.get(language_code, language_code)  # Default to code if not found
        
        details = {
            "title": data['title'],
            "poster_path": data['poster_path'],
            "overview": data['overview'],
            "release_date": data['release_date'],
            "runtime": data['runtime'],
            "vote_average": data['vote_average'],
            "language": language,  # Use full language name
            "cast": [member['name'] for member in data['credits']['cast'][:5]],
            "id": data['id']  # Added movie ID for linking
        }
        return details
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return {}

if __name__ == '__main__':
    app.run(debug=True)
