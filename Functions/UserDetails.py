import pandas as pd


def GetUserDetails(userinput):
    mysheet = 'Opera Passwords'
    file_loc = 'D:\Virtual Assistant\Database\Opera Passwords.xlsx'

    excel_data = pd.read_excel(file_loc, sheet_name=mysheet)


    site_names = excel_data['NAME']
    site_nameslst = site_names.tolist()

    final_df = pd.DataFrame(columns = ['NAME', 'USERNAME', 'PASSWORD', 'URL'])


    for name in site_nameslst:
        if userinput in name:
            indexes = site_names[site_names.isin([name])].index
            result = excel_data.loc[indexes]

            final_df = pd.concat([final_df, result], axis=0, join='outer', ignore_index=True)

        else:
            return f'Sir I could not find any saved credentials for {userinput}'

    return final_df
