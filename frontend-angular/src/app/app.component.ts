import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule, HttpClient } from '@angular/common/http';

interface Bike {
  id: number;
  modelName: string;
  category: string;
  dailyRate: number;
  available: boolean;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  template: `
    <div class="container">
      <header>
        <h1>Modern Bike Rental System</h1>
        <p>Built with Angular & Spring Boot</p>
        <button (click)="seedDatabase()" class="seed-btn">Seed Database (Demo)</button>
      </header>

      <div class="bike-list">
        <div class="bike-card" *ngFor="let bike of bikes">
          <h3>{{ bike.modelName }}</h3>
          <p class="category">{{ bike.category }}</p>
          <p class="rate">\${{ bike.dailyRate }} / day</p>
          
          <div class="actions">
            <span class="status" [class.available]="bike.available" [class.unavailable]="!bike.available">
              {{ bike.available ? 'Available' : 'Rented' }}
            </span>
            <button *ngIf="bike.available" (click)="rentBike(bike.id)" class="rent-btn">
              Rent Now
            </button>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .container { font-family: Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; }
    header { text-align: center; margin-bottom: 30px; }
    .seed-btn { background: #607d8b; color: white; border: none; padding: 8px 15px; border-radius: 4px; cursor: pointer; }
    .bike-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
    .bike-card { border: 1px solid #eee; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .category { color: #888; font-size: 0.9em; margin-bottom: 10px; }
    .rate { font-size: 1.2em; font-weight: bold; color: #333; }
    .actions { display: flex; justify-content: space-between; align-items: center; margin-top: 15px; }
    .status { padding: 4px 8px; border-radius: 12px; font-size: 0.8em; font-weight: bold; }
    .available { background: #e8f5e9; color: #2e7d32; }
    .unavailable { background: #ffebee; color: #c62828; }
    .rent-btn { background: #2196f3; color: white; border: none; padding: 6px 12px; border-radius: 4px; cursor: pointer; }
    .rent-btn:hover { background: #1976d2; }
  `]
})
export class AppComponent implements OnInit {
  bikes: Bike[] = [];
  apiUrl = 'http://localhost:8080/api/bikes';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.fetchBikes();
  }

  fetchBikes() {
    this.http.get<Bike[]>(this.apiUrl).subscribe({
      next: (data) => this.bikes = data,
      error: (err) => console.error('Error fetching bikes', err)
    });
  }

  seedDatabase() {
    this.http.post(this.apiUrl + '/seed', {}, { responseType: 'text' }).subscribe(() => {
      this.fetchBikes();
    });
  }

  rentBike(id: number) {
    this.http.post(\`\${this.apiUrl}/\${id}/rent\`, {}, { responseType: 'text' }).subscribe({
      next: () => {
        alert('Bike rented successfully!');
        this.fetchBikes();
      },
      error: (err) => alert('Error renting bike')
    });
  }
}
