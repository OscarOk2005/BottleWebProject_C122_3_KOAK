% rebase('layout.tpl', title=title, year=year)
<div class="container">
        <h1 class="text-center mb-3">Калькулятор метода Дейкстры</h1>
        <p class="text-center">Здесь вы можете ввести данные для метода Дейкстры и найти минимальное расстояние от указанной точки.</p>
        <form class="mb-3" action="/daykstra_result"  id="matrix_form">
            <div class="form-group">
                <label for="matrix_size">Размерность матрицы</label>
                <input type="number" class="form-control" id="matrix_size" name="matrix_size" min="3" max="10" required/>
                
                <label class="inputLabel" for="start_point">Начальная вершина</label>
                <input type="number" class="form-control" id="start_point" name="start_point" min="1" max="10" required/>
            </div>
            <button type="button" class="btn btn-primary" onclick="createMatrix()">Создать матрицу</button>
             <button value="send" type="submit" class="btn btn-primary" >Создать матрицу</button>
        </form>
        <div id="matrixContainer"></div>
</div>
    <script src="/static/scripts/matrix.js">
    </script>