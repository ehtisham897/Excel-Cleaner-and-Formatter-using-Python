import pandas as pd

def clean_excel(file_path, output_path):
    try:
        # Excel file read karo
        df = pd.read_excel(file_path)

        # Unwanted columns hatao (e.g. columns jinka naam 'Unnamed' se start hota hai)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Column names clean karo (lowercase, space replace with underscore)
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        # Missing values ko 0 se fill karo
        df.fillna(0, inplace=True)

        # Final file save karo
        df.to_excel(output_path, index=False)
        print(f" File cleaned and saved as: {output_path}")

    except Exception as e:
        print(" Error occurred:", e)

# Example usage
if __name__ == "__main__":
    input_file = "sample_excel_data.xlsx"      # Yeh tumhari input file hogi
    output_file = "cleaned_output.xlsx"        # Yeh tumhara output file hoga
    clean_excel(input_file, output_file)
