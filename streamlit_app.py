import streamlit as st
import requests

# Fetch players from SportsData.io API
@st.cache_data
def fetch_players():
    url = "https://api.sportsdata.io/v3/nba/stats/json/PlayerSeasonStats/2025"
    headers = {"Ocp-Apim-Subscription-Key": "0f830c9349244aadb70f735310c3afa0"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        st.error("Failed to load player data.")
        return []

    data = response.json()

    # Transform the data into simplified player objects with positions and a ranking
    simplified_players = []
    for idx, player in enumerate(data, start=1):  # use `idx` as ranking
        name = player.get("Name", "Unknown")
        position_str = player.get("Position", "")
        if not name or not position_str:
            continue
        positions = [pos.strip().upper() for pos in position_str.split("-") if pos]
        simplified_players.append({
            "name": name,
            "positions": positions,
            "ranking": idx
        })

    return simplified_players

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
        return [player for player in players if int(player["ranking"]) >= best_player_ranking]
    else:
        st.error("No matching players found.")
        return []

# Count positions of players
def count_positions(my_player_info):
    priority_list = {"C": 0, "SF": 0, "SG": 0, "PF": 0, "PG": 0}
    for player in my_player_info:
        positions = player["positions"]
        for position in positions:
            position = position.strip().upper()
            if position in priority_list:
                priority_list[position] += 1
    return priority_list

# Suggest best players to draft based on needed positions
def best_players(priority_list, available_players):
    needed_positions = [position for position, count in priority_list.items() if count == 0]
    st.write("### Best Players to Draft:")

    if needed_positions:
        for position in needed_positions:
            st.write(f"**Top players for position {position}:**")
            position_players = [player for player in available_players if position in player["positions"]]
            position_players = sorted(position_players, key=lambda x: x['ranking'])[:3]
            for player in position_players:
                st.write(f"- {player['name']}")
    else:
        st.write("You have filled all required positions. Here are the top available players:")
        all_available_players = sorted(available_players, key=lambda x: x['ranking'])[:5]
        for player in all_available_players:
            st.write(f"- {player['name']}")

# Main function for Streamlit app
def main():
    st.title("🏀 Fantasy Draft Helper")
    st.sidebar.header("Player Selection")

    players = fetch_players()

    if players:
        my_player_info = collect_lineup(players)

        if my_player_info:
            priority_list = count_positions(my_player_info)
            best_player_ranking = st.sidebar.text_input("Enter the best available player ranking in your draft (1–500):", "")

            if st.sidebar.button("Find Available Players"):
                available_players_list = available_players(players, best_player_ranking)
                if available_players_list:
                    best_players(priority_list, available_players_list)
    else:
        st.error("No players data found.")

if __name__ == "__main__":
    main()
