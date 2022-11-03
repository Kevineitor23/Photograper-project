from pexels_api import API
apisk = '563492ad6f91700001000001b52ff90768744b9089f32109f67d6503'

api = API(apisk)

api.search('kitten', page=1, results_per_page=5)

photos = api.get_entries()


for photo in photos:
  # Print photographer
  print('Photographer: ', photo.photographer)
  # Print url
  print('Photo url: ', photo.url)
  # Print original size url
  print('Photo original size: ', photo.original)


