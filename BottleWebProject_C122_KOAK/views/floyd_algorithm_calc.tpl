% rebase('layout.tpl', title='Floyd algorithm calculator', year=year)
<div class="container">
        <h1 class="text-center mb-3">Калькулятор алгоритма Флойда</h1>
        <p class="text-center">Здесь вы можете ввести данные для алгоритма Флойда и найти все кратчайшие пути для графа</p>
        %include('matrix.tpl')
        <div id="matrixContainer"></div>
    </div>
            <script src="/static/scripts/matrix.js">
    </script>
