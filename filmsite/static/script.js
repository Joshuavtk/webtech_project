window.onload = () => {

    let genres = document.getElementById('checked_genres')
    if (genres) {
        console.log(genres)
        genres = genres.innerHTML.split(' ')
        genres.forEach(genre => {
            if (genre) {
                document.getElementById('genres-' + (genre - 1)).checked = true
            }
        });
    }
    
}