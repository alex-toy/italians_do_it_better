# 1.2 FUNCTION TO CHECK UNIQUE NON-NULL AND NON'' (empty) VALUES IN A COLUMN
def unique_clean(data,col,pr=0):
    u=data[col].unique()
    clean=[]
    for m in u:
        if (pd.isna(m)==False and m!=''):
            clean.append(m)
            if pr!=0:
                print(m)

    print('\nnumber of ',data[col].name,' unique (non null) values: ',len(clean))
    print(type(clean),'\n')
    return clean


#CHECKOUT FOR SPECIFIC VALUES IN A COLUMN

# function to extract a dataframe with a specific text contained in a dataframe column 
def df_with_text(data,col,text):
    col_contains_text = data[col].str.contains(text, regex=True, case=False)
    col_contains_text[col_contains_text.isna()]=False
    data[col_contains_text].head()
    return data[col_contains_text]

# function to get rows with 1 specific text (string) in a dataframe column 
def text_in_df(data,col,text):
    data_extract=df_with_text(data,col,text)
    temp = data_extract[col].unique()
    values_containing_text = pd.DataFrame(list(filter(lambda a: a != "nan",temp )))
    print('text "',text,'appears',data_extract.shape[0],'lines, in',len(values_containing_text),'different values')
    return values_containing_text

# function to get rows with 2 specific text (string) in a dataframe column 
def two_text_in_df(data,col,text1,text2):
    temp = text_in_df(data,col,text1)
    return text_in_df(temp,0,text2)
    
def values_U_not_nan(data,col_name):
    col_nan = data[col_name].isna() #list de bolean True/False (initial length)
    col_not_nan = ~ col_nan # ~ is used to inverse bolean values
    col_U = data[col_name][col_not_nan]
    return sorted(col_U.unique())
    
# the hat ^ or $ enables to lookup an exact word ! => 690 values
# ^ ENTIRE STRING start by text we are looking for
# $ ENTIRE STRING ends by text we are looking for
# https://javascript.info/regexp-anchors         
# ' FER ' fore an entire word can work too (' FER' or 'FER ')


# ABC function to get rows with 2 specific texts (string) in a dataframe column 
def two_text_in_df(data,col,text1,text2=''):
    data_extract=df_with_text(data,col,text1)
    temp = data_extract[col].unique()
    values_containing_text = pd.DataFrame(list(filter(lambda a: a != "nan",temp )))
    if text2=='':
        print('text "',text1,'"appears',data_extract.shape[0],'lines, in',len(values_containing_text),'different values')
    if text2!='':
        print('first text "',text1,'" alone appears',data_extract.shape[0],'lines, in',len(values_containing_text),'different values and with')
        values_containing_text=text_in_df(values_containing_text,0,text2)
    return values_containing_text


#---------------------------------------------------------------------
#---------------------------------------------------------------------
# 1.3 FUNCTION TO GET INDEX OF NON-NULL AND NON'' (empty) VALUES IN A COLUMN
def not_nan_get_values(data,col_name,pr=0):
    col_nan = data[col_name].isna() #list de bolean True/False (initial length)
    col_not_nan = ~ col_nan # ~ is used to inverse bolean values
    col_U = data[col_name][col_not_nan].unique()
    if pr != 0:
        print('number of change in KPIs:',len(col_U),'\n')
        print('index of not nan values:')
        print('\n',col_U)
    return col_U

def not_nan_get_index(data, col_name, pr=0):
    col_nan = data[col_name].isna() #list de bolean True/False (initial length)
    col_U = data[col_name][~col_nan]
    if pr!=0:
        print('number of non nan values:',len(col_U),'\n')
        print('index of not nan values:')
        print('\n',col_U)
    return col_U.index

def nan_get_index(data, col_name, pr=0):
    col_nan = data[col_name].isna() #list de bolean True/False (initial length)
    col_U = data[col_name][col_nan]
    if pr!=0:
        print('number of nan values:',len(col_U),'\n')
        print('index of nan values:')
        print('\n',col_U)
    return col_U.index


# "VECTOR FUNCTION" TO CHECK IF ALL VALUE IN NP ARRAY ARE DECIMAL VLAUES
def is_not_decimal(a):
    return not np.char.isdecimal(a)

#v_is_not_decimal = np.vectorize(is_not_decimal)
#PB_num=v_is_not_decimal(ITEM)
#print('number of EAN with non numerical values',PB_num.sum())
#ITEM[PB_num]


# "VECTOR FUNCTION" TO CHECK IF ALL VALUE IN NP ARRAY ARE DECIMAL VLAUES
def is_not_13(a):
    return len(a)!=13

#v_is_not_13 = np.vectorize(is_not_13)
#PB_13=v_is_not_13(ITEM)
#print('number of EAN which do not have 13 digits',PB_13.sum())
#sITEM[PB_13]


#Split item on text (str) and return left or right side of the split
def split_item_left(st) :
    if isinstance(st[0], str) and isinstance(st[1], str) :
        return st[0].split(st[1], 1)[0] # keep first part [0] of split (before the splitter (st[1])
    elif isinstance(st[0], str) :
        return st[0]

def split_item_right(st) :
    if isinstance(st[0], str) and isinstance(st[1], str) :
        split=st[0].split(st[1], 1)
        if len( split)>1:
            return st[0].split(st[1], 1)[1]  # keep second part [1] of split (after the splitter (st[1])
    elif isinstance(st[0], str) :
        return st[0]




