% rebase('layout.tpl', title='Prima algorithm calculator', year=year)
<div class="container">
<form action="/prima_result" method="POST"  id="matrix_form">
        <h1 class="text-center header-page">Калькулятор алгоритма Прима</h1>
        <p class="text-center">Здесь вы можете ввести данные для алгоритма Прима и найти минимальное остовное дерево</p>
        %include('matrix.tpl')
        <div id="matrixContainer"></div>
        </form>
    </div>
            <script src="/static/scripts/matrix.js">
    </script>

