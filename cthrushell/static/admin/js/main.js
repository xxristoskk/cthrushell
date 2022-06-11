if (document.querySelector('.side-nav').style.width == '0') {
    const button = `
        <div class='menu'>
            <a href='http://cthrushell.com/#'><h3>XKXK</h3></a>
        </div>
    `
    document.querySelector('#mobile-button').innerHTML += button

    document.querySelector('.menu').addEventListener('click', function() {
        document.querySelector('.side-nav').style.width = '60'
    })

}

// const thumbBarImg = ["{% static 'admin/img/glitch-bg.png' %}", 
// "{% static 'admin/img/flower2.png' %}",
// "{% static 'admin/img/flowers3.jpg' %}",
// "{% static 'admin/img/alien000.jpg' %}",
// "{% static 'admin/img/cherry_blossoms2.jpg' %}",
// "{% static 'admin/img/cyborg_eyes.jpg' %}",
// "{% static 'admin/img/flower-glitch1000.jpg' %}",
// "{% static 'admin/img/flower-glitch2000.jpg' %}",
// "{% static 'admin/img/me.jpeg' %}",
// "{% static 'admin/img/plant_glitch.jpg' %}",
// "{% static 'admin/img/self_glitch.jpg' %}",
// "{% static 'admin/img/space_ribbons.jpg' %}",
// "{% static 'admin/img/statue.jpg' %}"]

// for (let i = 0; i < thumbBar.length; i++) {
//     document.getElementById('thumb-bar').innerHTML += 
//     `<img src=${thumbBar[i]} class='thumb'>`
// }

// const thumbs = Array.from(document.getElementsByClassName('thumb'))

// thumbs.forEach(function(element) {
//     element.addEventListener('click', function() {

//         document.getElementById('displayed').src = element.src
//         document.getElementById('feat-item').innerHTML = element
//     })
// })