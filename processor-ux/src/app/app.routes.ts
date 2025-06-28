import { Routes } from '@angular/router';
import { ProcessingComponent } from './processing/processing.component';

export const routes: Routes = [
    { path: '', redirectTo: 'processing', pathMatch: 'full' },
    { path: 'processing', component: ProcessingComponent }
];
