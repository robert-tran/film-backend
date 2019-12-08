# Obtain these from the sar_webservice_poc and lgbm_webservice_pos notebook linked in the recommenders repository
sar_url = 'http://52.187.71.186:80/api/v1/service/aksrecosar1m/score'
sar_token = 'Bearer N26FgGiDmeRYnC9cAqwk8dyae7Beiw9v'
# lgbm_url = LGBM_MODEL_ENDPOINT
# lgbm_token = LGBM_BEARER_TOKEN

# Obtain these from the "Setting up Azure SQL Database" step
server = 'tcp:admin-sang.database.windows.net'
database = 'MOVIES'
username = 'admin-sang'
password = 'Robert_251298'
driver = '{ODBC Driver 13 for SQL Server}'
api_key = 'B47D6998EBC4D8997CC9EC480E7E08C6'

# Obtain the API key from the tmdb website listed in the prerequisites
tmdb_key = 'd1ddc0e2dbd32aba1cf4cc30bdb8bb43'

# Obtain from the "Setting up Azure Search" step
search_url = 'https://search-for-app.search.windows.net/indexes/film-index/docs?api-version=2019-05-06&search='