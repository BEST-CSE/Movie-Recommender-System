import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6c72dcf33d8559368a457d38228be17f&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    recommanded_movie_list = sorted(list(enumerate((distances))), reverse=True, key=lambda x: x[1])[1:11]


    recommended_movies = []
    recommended_movies_poster = []
    for i in recommanded_movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommender System')

selected_movies_name = st.selectbox(
"Search for recommended movies",
movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movies_name)

    # col1 = st.columns(1)
    # for i in range(0, 9):
    #     cols = st.columns(3)
    #     st.header(names[i])
    #     st.image(posters[i])
    # First "row"
    col1, col2 = st.columns(2)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])


    # Second "row"
    col3, col4 = st.columns(2)
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])

    # Third "row"
    col5, col6 = st.columns(2)
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])

    # Fourth "row"
    col7, col8 = st.columns(2)
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])

    # Fifth "row"
    col9, col10 = st.columns(2)
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
    # with row1:
    #     st.header(names[0])
    #     st.image(posters[0])
    # with row2:
    #     st.header(names[1])
    #     st.image(posters[1])
    # with row3:
    #     st.header(names[2])
    #     st.image(posters[2])
    # with row4:
    #     st.header(names[3])
    #     st.image(posters[3])
    # with row5:
    #     st.header(names[4])
    #     st.image(posters[4])
    # with row6:
    #     st.header(names[5])
    #     st.image(posters[5])
    # with row7:
    #     st.header(names[6])
    #     st.image(posters[6])
    # with row8:
    #     st.header(names[7])
    #     st.image(posters[7])
    # with row9:
    #     st.header(names[8])
    #     st.image(posters[8])
    # with row10:
    #     st.header(names[9])
    #     st.image(posters[9])