from model.menu_manage import *
from model.order_manage import *
import pickle

if __name__ == "__main__":
    with open('menu.pickle', 'rb') as f:
        menus = pickle.load(f)
        print("menus data Loaded Successfully")
    
    breakfast_menu = menus["Breakfast"]
    lunch_menu = menus["Lunch"]

    # Adding items to Breakfast menu
    menu_manager = MenuManager()
    breakfast_menu = menu_manager.get_menu("Breakfast")
    breakfast_menu.add_item("Poori", 30, "Deep-fried Indian bread, made from unleavened wheat dough, served fluffy and puffed.", "poori.jpg", "Breakfast")
    breakfast_menu.add_item("Idly", 8, "Steamed, spongy rice and urad dal dumplings, a staple in South Indian cuisine", "Idly.jpg", "Breakfast")
    breakfast_menu.add_item("Dosa", 40, "Thin, crispy fermented rice and urad dal crepe, a versatile dish in Indian cuisine.", "plain-dosa.jpg", "Breakfast")
    breakfast_menu.add_item("Vadai", 10, "Deep-fried lentil fritters, typically made with urad dal or chana dal, enjoyed as a savory snack.", "medhu-vadai.jpg", "Breakfast")
    breakfast_menu.add_item("Pongal", 40, "South Indian rice dish cooked with lentils, black pepper, cumin, and ghee, often garnished with cashews.", "rava-pongal.jpg", "Breakfast")
    breakfast_menu.add_item("Upma", 35, "A savory South Indian dish made from dry-roasted semolina, typically seasoned with mustard seeds, curry leaves, and vegetables.", "upma.jpg", "Breakfast")
    breakfast_menu.add_item("Aloo Parota", 105, "Aloo Parota, An Indian flatbread with spiced mashed potatoes, pan-fried golden, served with yogurt or pickles.", "aloo-parota.jpg", "Breakfast")
    breakfast_menu.add_item("Double Omelette", 30, "Double Omelette, a protein-packed breakfast, features two perfectly cooked layers, served with toast for a delicious start.", "omelette.jpg", "Breakfast")
    

    # Adding items to Lunch menu
    lunch_menu = menu_manager.get_menu("Lunch")
    lunch_menu.add_item("Chicken Biriyani", 150, "A flavorful Indian rice dish with aromatic basmati rice, chicken, and a blend of spices, cooked to perfection.", "chicken-biriyani.png", "Lunch")
    lunch_menu.add_item("Pizza", 100, "Oven-baked flatbread topped with tomato sauce, cheese, and various toppings, a popular Italian dish enjoyed worldwide.", "pizza.jpg", "Lunch")
    lunch_menu.add_item("Mutton Biriyani", 200, "Savor the richness of spiced rice and tender mutton in this flavorful Indian biryani, a hearty and aromatic culinary indulgence.", "mutton-biriyani.jpg", "Lunch")
    lunch_menu.add_item("Sandwich", 160, "A versatile and convenient meal, typically consisting of layers of ingredients such as bread, vegetables, cheese, and meats.", "sandwich.jpg", "Lunch")
    lunch_menu.add_item("Sambar Rice", 30, "A comforting South Indian dish where rice is combined with sambar, a tangy and spicy lentil-based vegetable stew.", "sambar.jpg", "Lunch")
    lunch_menu.add_item("Veg Fried Rice", 80, "Stir-fried rice with mixed vegetables, often seasoned with soy sauce and spices, creating a flavorful and quick vegetarian dish.", "veg-fried-rice.jpg", "Lunch")
    lunch_menu.add_item("Curd Rice", 30, "A simple South Indian dish combining rice with yogurt, often tempered with mustard seeds, curry leaves, and green chillies.", "curd-rice.jpg", "Lunch")
    lunch_menu.add_item("Full Meals", 80, "A balanced Indian meal: rice, chapati, curry, dal, veggies, and dessert - a wholesome dining experience in one plate.", "meals.jpg", "Lunch")

    menus = {
        "Breakfast": menu_manager.get_menu("Breakfast"),
        "Lunch": menu_manager.get_menu("Lunch"),
        "Snacks": menu_manager.get_menu("Snacks"),
        "Drinks": menu_manager.get_menu("Drinks"),
        "Dinner": menu_manager.get_menu("Dinner"),
        "Dessert": menu_manager.get_menu("Dessert")
    }


    try:
        with open('menu.pickle', 'wb') as file:
            pickle.dump(menus, file)
            print("Data Written Successfully")
    except Exception as e:
        print(f"Error saving menus: {e}")
    