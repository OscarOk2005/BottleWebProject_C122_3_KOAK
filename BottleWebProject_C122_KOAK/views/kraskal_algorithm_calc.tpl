% rebase('layout.tpl', title='Kraskal algorithm calculator', year=year)
<div class="container">
<form action="/kraskal_result" method="POST"  id="matrix_form">
        <h1 class="text-center header-page">Калькулятор алгоритма Краскала</h1>
        <p class="text-center">Здесь вы можете ввести данные для алгоритма Краскала и найти минимальное остовное дерево</p>
        %include('matrix.tpl')
        
        </form>
    </div>
            <script src="/static/scripts/matrix.js">
    </script>

