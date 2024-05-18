% rebase('layout.tpl', title=title, year=year)
<div class="container">
	<div class="theory-block">
		<h3>Результат</h3>
		<p>
			{{message}}
			<img src="static/images/Graph.png"></img>
		</p>
		% from math import sqrt
		% import numpy as np
		% data = np. array(data)
		% if data.size == 1:
		<p>Суммарный вес искомого MST = {{int(data)}}</p>
		% else:
		<p>
			Граф выше может быть представлен следующей матрицей смежности:
		</p>
	
		<div class="resultTable">
		<table>
			% for i in range (int(sqrt(data.size) + 1)):
			<tr > 
				% for j in range (int(sqrt(data.size) + 1)):
					%if (i + j != 0):
						%if (i == 0 or j == 0):
							<th => 
								{{i + j}}
							</th>
						%else:
							%if (data[i - 1, j - 1] != -1):
								<th class="resultTableCell"> 
									{{int(data[i - 1, j - 1])}}
								</th>
							%else:
							<th class="resultTableCell"> 
									∞
								</th>
							%end
						%end
					%else:
						<th class="resultTableHeader"> 
						</th>
					%end
				%end
			</tr>
			%end
			</table>
		</div>
		%end
	</div>
</div>
