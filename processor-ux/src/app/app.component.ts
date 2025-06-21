import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ClarityModule } from "@clr/angular";
import { HeaderComponent } from "./header/header.component";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ClarityModule, HeaderComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'CJ Transformer';
}
