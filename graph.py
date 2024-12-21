graph = {
    'Jain University Gate': {'Golf course': 100, 'Short-cut near Non IT building': 350},
    'Golf course': {'Jain University Gate': 100, 'FET (MAIN)': 300},
    'FET (MAIN)': {'Golf course': 300, 'FET (BACK)': 97},
    'FET (BACK)': {'FET (MAIN)': 97, 'Mess': 44, 'Himalayas': 63},
    'Himalayas': {'FET (BACK)': 63, 'Mess': 71},
    'Mess': {'FET (BACK)': 44, 'Himalayas': 71, 'Purvanchal': 71},
    'Purvanchal': {'Mess': 71, 'Karakoram': 39},
    'Karakoram': {'Purvanchal': 39, 'Football field': 160},
    'Football field': {'Karakoram': 160, 'Tennis court': 98, 'Short-cut near Non IT building': 240 },
    'Tennis court': {'Football field': 98, 'Sprintoor': 180, 'Sai Baba temple': 180},
    'Sprintoor': {'Tennis court': 180, 'Swimming Pool': 54},
    'Swimming Pool': {'Sprintoor': 54},
    'Sai Baba temple': {'Tennis court': 180, 'Non IT building': 250, 'Colosseum': 130},
    'Colosseum': {'Sai Baba temple': 130},
    'Short-cut near Non IT building': {'Jain University Gate': 350, 'Non IT building': 120, 'Football field': 240},
    'Non IT building': {'Short-cut near Non IT building': 120, 'Sai Baba temple': 250}
}
