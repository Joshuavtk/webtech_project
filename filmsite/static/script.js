window.onload = () => {

    let genres = document.getElementById('checked_genres')
    if (genres) {
        let list_genres = document.getElementById('genres').children
        genres = genres.innerHTML.trim().split(' ').map(e => parseInt(e))
        for (let i = 0; i < list_genres.length; i++) {
            let element = list_genres[i].firstChild;
            if (genres.includes(parseInt(element.value))) {
                element.checked = true
            }
            
        }
    }
    
}