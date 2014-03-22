from PrismAPI.Main import PrismAPI

if __name__ == '__main__':
    p_id = '62404'
    prism = PrismAPI.PrismAPI()
    prism.set_basic_auth("brigglere","13S!ri-3")
    results = prism.search_people(['programmer'],25,0)
    s_view = prism.simple_view(results)
    
    prism.write_to_csv("s_view.csv",results)
    
    
