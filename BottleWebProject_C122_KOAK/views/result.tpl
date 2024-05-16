% rebase('layout.tpl', title=title, year=year)
<div class="container">
	<div class="theory-block">
		<h3>Результат</h3>
		<p>
			{{message}}
			<img src="static/images/Graph.png"></img>
		</p>
		<p>
			Граф выше может быть представлен следующей матрицей смежности:
		</p>
		<table >
		% for i in range (6):
		<tr > 
			% for j in range (6):
				%if (i + j != 0):
					%if (i == 0 or j == 0):
						<th => 
							{{i + j}}
						</th>
					%else:
						<th class="resultTableCell"> 
							{{i + j}}
						</th>
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
</div>
