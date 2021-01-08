console.log("This is Dar's js file");

fetch('https://reqres.in/api/users?page=2').then(response => response.json()).then(responseJSON => createUserList(responseJSON.data))
 .catch(err =>console.log(err)); //fetch function 


function createUserList(users){
    console.log(users);
    const curr_main = document.querySelector("main");
    for (let user of users) {
        const section =document.createElement("section");
                    section.innerHTML=
            `<img src="${user.avatar}" alt="Profile Picture"/>
            <div>
                <span>${user.first_name} ${user.last_name}</span>
                <br>
                <a herf="mailto:${user.email}">Send Email</a>
            </div>
            `;
        curr_main.appendChild(section);
    
    } 
    
}


 