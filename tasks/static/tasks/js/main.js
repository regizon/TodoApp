document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded');


    const editButtons = document.getElementsByClassName("edit_button");
    for(let btn of editButtons){
        btn.onclick = function () {
            const taskId = btn.id;
            const parent = btn.parentNode;
            console.log(parent);
            const tdParent = parent.parentNode;
            const trParent = tdParent.parentNode;
            console.log(trParent);
            const previousText = trParent.querySelector("span")
            console.log(previousText);
            let inputText = document.createElement('input');
            inputText.value = previousText.textContent;
            inputText.name = "title";
            const newForm = document.createElement('form');
            const submitButton = document.createElement("input");
            const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            const csrfInput = document.createElement('input');
            csrfInput.type = "hidden";
            csrfInput.name = "csrfmiddlewaretoken";
            csrfInput.value = csrfToken;
            submitButton.type = "submit";
            submitButton.name = taskId;
            submitButton.value = "Save";
            submitButton.classList.add("btn-success");
            newForm.action = "updateTask";
            newForm.method = "POST";
            newForm.appendChild(inputText);
            newForm.appendChild(submitButton);
            newForm.appendChild(csrfInput);
            previousText.parentNode.replaceChild(newForm, previousText);
        }
    }


    const allDropdownMenus = document.querySelectorAll(".dropdown-menu");
    console.log('Found dropdown menus:', allDropdownMenus.length);


    function changePriority(clickedLi) {
        let btnGroup = clickedLi.closest('.btn-group')
        let firstButton = btnGroup.querySelector(".dropdown-toggle");
        let chosenButton = clickedLi.querySelector("button");
        let form = clickedLi.closest('form')
        let priorityInput = form.priority;


        console.log(chosenButton.id);
        let mainText = firstButton.textContent;
        let chosenText = chosenButton.textContent;

        let mainClasses = Array.from(firstButton.classList);
        let chosenClasses = Array.from(chosenButton.classList);

        firstButton.textContent = chosenText;

        chosenButton.textContent = mainText;

        const mainColorClasses = Array.from(firstButton.classList).filter(cls => cls.startsWith('btn-') && cls !== 'btn');
        const clickedColorClasses = Array.from(chosenButton.classList).filter(cls => cls.startsWith('btn-') && cls !== 'btn');


        let newPriority = '';
        console.log(clickedColorClasses)
        if (clickedColorClasses.includes('btn-danger')) {
            newPriority = '1';
        }
        else if (clickedColorClasses.includes('btn-warning')) {
            newPriority = '2';
        }
        else {
            newPriority = '3';
        }

        priorityInput.value = newPriority;
        form.submit()

        // Убираем старые цветовые классы
        mainColorClasses.forEach(cls => firstButton.classList.remove(cls));
        clickedColorClasses.forEach(cls => chosenButton.classList.remove(cls));

        // Устанавливаем новые классы
        firstButton.classList.add(...chosenClasses.filter(cls =>
            cls.startsWith('btn-') && cls !== 'btn'
        ));
        
        chosenButton.classList.add(...mainClasses.filter(cls =>
            cls.startsWith('btn-') && cls !== 'btn' && cls !== 'dropdown-toggle'
        ));
        
        // Устанавливаем dropdown атрибуты
        firstButton.setAttribute('data-bs-toggle', 'dropdown');
        firstButton.setAttribute('aria-expanded', 'false');
        
        // Убираем dropdown атрибуты с кликнутой кнопки
        chosenButton.removeAttribute('data-bs-toggle');
        chosenButton.removeAttribute('aria-expanded');

    }

    allDropdownMenus.forEach(dropdown => {
        for (const liChild of dropdown.children) {
            const button = liChild.querySelector('button');
            if (button) {
                button.addEventListener("click", function (event) {
                    changePriority(liChild);
                });
            }
        }
    });
});