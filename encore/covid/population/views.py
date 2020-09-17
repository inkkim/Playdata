from django.shortcuts import render

# Create your views here.
import pandas as pd

def main_view1(request):
    df = pd.read_csv(f'/Users/ink/Playdata/09/20200916/pop_by_date.csv')
    labels = list(df['STDR_DE_ID'].values)
    data = list(df['TOT_LVPOP_CO'].values)

    return render(request, 'bar-chart.html', {
        'labels': labels,
        'data': data,
   })

def main_view2(request):
    df1 = pd.read_csv(f'/Users/ink/Playdata/09/20200916/pop_by_gu.csv')
    df2 = df1.groupby('name', as_index=False).mean()
    labels2 = list(df2['name'].values)
    data2 = list(df2['TOT_LVPOP_CO'].values)
    #print(df1.columns)
    df1.drop(['ADSTRD_CODE_SE'], inplace = True, axis = 1)
    data_89 = list(df1.loc[df1['STDR_DE_ID'] == 20200809]['TOT_LVPOP_CO'].values)
    print(data_89)
    return render(request, 'bar-chart2.html', {
        'labels2': labels2,
        'data2': data2,
        'data_89': data_89,
    })