from services.data_loader import data_loader
from services.dashboard import Dashboard

def main() -> None:
    """
    Main function.
    """
    # Load the data
    database = data_loader('../db/Equity Selection.xlsx')
    # Print the data
    
    # print(database.get_equities())
    # print(database.get_data())
    
    
    dashboard = Dashboard(data=database.get_data())
    
    dashboard.run()


if __name__ == "__main__":
    main()