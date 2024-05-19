            <div class="form-group">
                <label for="matrix_size" title='Целое число от 3 до 10'>Размерность матрицы</label>
                <input type="number" class="form-control" onkeydown="return event.key !== 'Enter' && event.key !== '-'" id="matrix_size" name="matrix_size" min="3" max="10" required/>
            </div>
            <button id="create-matrix-button" type="button" class="btn btn-primary" onclick="createMatrix()">Создать матрицу</button>
        <div id="matrixContainer"></div>