import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { ClarityModule } from '@clr/angular';

@Component({
  selector: 'app-header',
  imports: [ClarityModule, RouterModule],
  templateUrl: './header.component.html',
  styleUrl: './header.component.scss'
})
export class HeaderComponent {

  readonly appBrandRoute: RouteDefinition = {
    label: 'CJ Transformer',
    route: '/'
  };

  readonly menuRoutes: RouteDefinition[] = [
    { label: 'Home', route: '/' }
  ];

}

export interface RouteDefinition {

  label: string;
  route: string;
}
