import pandas as pd

def csv_to_markdown_simple(csv_file_path, md_file_path):
    df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

    # Writing to a Markdown file
    with open(md_file_path, 'w', encoding='utf-8') as file:
        for index, row in df.iterrows():
            for col_index, col_value in enumerate(row):
                if col_index in [0, 4, 5, 6, 7, 11]:  # Replace with the indices of the columns you want
                    if col_index == 0:
                        file.write(f'# {col_value}. ')
                    elif col_index == 4:
                        file.write(f'{col_value} \n')
                    elif col_index == 5:
                        file.write(f'#### {col_value} ')
                    elif col_index == 6:
                        file.write(f'{col_value} \n')
                    elif col_index == 7:
                        file.write(f'\n{col_value} \n')
                    elif col_index == 11:
                        file.write(f'{col_value} \n')
                    else:
                        file.write(f'{col_value} \n')

            
            # Separator between rows
            file.write('\n---\n\n')

csv_file_path = 'projects.csv'  # path to your CSV file
md_file_path = 'output.md'  # path for new markdown file

csv_to_markdown_simple(csv_file_path, md_file_path)
