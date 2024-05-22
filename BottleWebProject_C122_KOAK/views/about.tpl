% rebase('layout.tpl', title=title, year=year)
<div class="container">
  <h1 class="text-center header-page">Наша команда</h1>

  <div class="row">
    % for member in team_members:
      <div class="col-md-6">
        <div class="card text-center h-100">
          <img src="{{member['image']}}" alt="{{member['name']}}" class="card-img-top rounded-circle mx-auto mt-3" style="width: 100px; height: 100px;">
          <div class="card-body">
            <h5 class="card-title">{{member['name']}}</h5>
            <p class="card-text">{{member['description']}}</p>
            <hr>
            <div class="d-flex justify-content-center">
              % for social_link in member['social_links']:
                        <a href="{{ social_link['url'] }}" target="_blank" id="{{member['name']}}-{{social_link['name']}}">
                            <img src="{{ social_link['icon'] }}" alt="{{ social_link['name'] }}" class="mx-1" style="width: 30px; height: 30px;">
                        </a>
                    % end
            </div>
          </div>
        </div>
      </div>
    % end
  </div>

  <div class="text-center">
    <a href="https://github.com/OscarOk2005/BottleWebProject_C122_KOAK" id="github-link" target="_blank" class="btn btn-primary">Наш GitHub</a>
  </div>
</div>
