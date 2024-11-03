import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json
import os

# Initialize Firebase inside a function to ensure it's not globally initialized
def init_firebase():
    if not firebase_admin._apps:
        # Option 1: Load credentials from a local JSON file
        # credentials_path = "fantasy-89e93-firebase-adminsdk-mok47-61639aeb61.json"

        # Option 2: Load credentials from an environment variable
        firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")
        if firebase_credentials:
            cred = credentials.Certificate(json.loads(firebase_credentials))
            firebase_admin.initialize_app(cred)
        else:
            raise ValueError("Firebase credentials not set in environment variables.")
    return firestore.client()

# Retrieve players data from Firebase
def retrieve_players_data():
    db = init_firebase()
    collection_name = "ReadPlayers" 
    players_ref = db.collection(collection_name)
    docs = players_ref.stream()
    players = [doc.to_dict() for doc in docs]
    return players

# Collect lineup from user input
def collect_lineup(players):
    st.write("### Select Your Players:")
    player_names = [player["name"] for player in players]
    selected_players = st.multiselect("Choose players to add to your lineup:", player_names)

    my_player_info = []
    for player_name in selected_players:
        matched_player = next((player for player in players if player["name"].strip().lower() == player_name.strip().lower()), None)
        if matched_player:
            my_player_info.append(matched_player)
            st.success(f"Added: {player_name}")
    
    return my_player_info

# Find available players to draft
def available_players(players, best_player_ranking):
    try:
        best_player_ranking = int(best_player_ranking)
    except ValueError:
        st.error("Invalid ranking value. Please enter a number.")
        return []

    matched_player = next((player for player in players if int(player["ranking"]) == best_player_ranking), None)
    if matched_player:
        return [player for player in players if int(player["ranking"]) <= best_player_ranking]
    else:
        st.error("No matching players found.")
        return []

# Count positions of players
def count_positions(my_player_info):
    priority_list = {"C": 0, "SF": 0, "SG": 0, "PF": 0, "PG": 0}
    for player in my_player_info:
        positions = player["positions"]
        if isinstance(positions, list):
            for position in positions:
                position = position.strip().upper()
                if position in priority_list:
                    priority_list[position] += 1
        else:
            position = positions.strip().upper()
            if position in priority_list:
                priority_list[position] += 1
    return priority_list

# Suggest best players to draft
def best_players(priority_list, available_players):
    needed_positions = [position for position, count in priority_list.items() if count == 0]
    st.write("### Best Players to Draft:")
    
    if needed_positions:
        for position in needed_positions:
            st.write(f"**Top players for position {position}:**")
            position_players = [player for player in available_players if position in player["positions"]]
            position_players = sorted(position_players, key=lambda x: x['ranking'], reverse=True)[:3]
            for player in position_players:
                st.write(f"- {player['name']}")
    else:
        sorted_items = sorted(priority_list.items(), key=lambda item: item[1])
        last_item = sorted_items[0]
        position_to_fill = last_item[0]
        best_players_for_position = [player for player in available_players if position_to_fill in player['positions']]
        best_players_for_position = sorted(best_players_for_position, key=lambda x: x['ranking'])[:3]
        st.write("You have filled all positions. Here are the top players available if you want to draft more:")
        # Sort all available players by ranking
        all_available_players = sorted(available_players, key=lambda x: x['ranking'])[:3]
        for player in all_available_players:
            st.write(f"- {player['name']} (Position: {player['positions']}, Ranking: {player['ranking']})")

# Main function for Streamlit app
def main():
    st.title("🏀 Fantasy Draft Helper")
    st.sidebar.header("Player Selection")

    # Call retrieve_players_data inside the main Streamlit context
    players = retrieve_players_data()
    
    if players:
        my_player_info = collect_lineup(players)
        
        if my_player_info:
            priority_list = count_positions(my_player_info)
            best_player_ranking = st.sidebar.text_input("Enter the best available player ranking:", "")
            
            if st.sidebar.button("Find Available Players"):
                available_players_list = available_players(players, best_player_ranking)
                if available_players_list:
                    best_players(priority_list, available_players_list)
    else:
        st.error("No players data found.")

if __name__ == "__main__":
    main()
