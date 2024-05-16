function createMatrix() {
    const size = document.getElementById('matrix_size').value;
    if (Number.isInteger(Number.parseInt(size))) {
        if (Number.parseInt(size) > 2 && Number.parseInt(size) < 11) {
            const container = document.getElementById('matrixContainer');
            container.innerHTML = '';

            const table = document.createElement('table');
            table.classList.add('table', 'table-bordered');

            const thead = document.createElement('thead');
            const headerRow = document.createElement('tr');

            const emptyCell = document.createElement('th');
            headerRow.appendChild(emptyCell);

            for (let j = 1; j <= size; j++) {
                const headerCell = document.createElement('th');
                headerCell.textContent = j;
                headerRow.appendChild(headerCell);
            }
            thead.appendChild(headerRow);
            table.appendChild(thead);

            const tbody = document.createElement('tbody');

            for (let i = 0; i < size; i++) {
                const row = document.createElement('tr');

                const rowNumberCell = document.createElement('th');
                rowNumberCell.textContent = i + 1;
                row.appendChild(rowNumberCell);

                for (let j = 0; j < size; j++) {
                    const cell = document.createElement('td');
                    const input = document.createElement('input');
                    input.type = 'number';
                    input.onkeydown = function (event) {
                        return event.key !== '-';
                    };
                    input.classList.add('form-control');
                    input.classList.add('matrix-input');
                    input.name = `matrix[${i}][${j}]`;
                    cell.appendChild(input);
                    row.appendChild(cell);
                }

                tbody.appendChild(row);
            }

            table.appendChild(tbody);
            container.appendChild(table);

            const submitButton = document.createElement('button');
            submitButton.type = 'submit';
            submitButton.classList.add('btn', 'btn-primary', 'mt-3');
            submitButton.textContent = 'Рассчитать';
            container.appendChild(submitButton);
        }
        else {
            alert("Ошибка");
        }
    }
    else {
        alert("Ошибка");
    }
}