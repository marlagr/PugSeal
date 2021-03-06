import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { DatePipe } from '@angular/common'

import { AppRoutingModule } from './app.routing';
import { NavbarModule } from './shared/navbar/navbar.module';
import { FooterModule } from './shared/footer/footer.module';
import { SidebarModule } from './sidebar/sidebar.module';

import { AppComponent } from './app.component';
import { ModalModule } from 'ngx-bootstrap/modal';

import { AdminLayoutComponent } from './layouts/admin-layout/admin-layout.component';
import { MantenimientoPreventivoComponent } from './admin/mantenimiento-preventivo/mantenimiento-preventivo.component';
import { MantenimientoPreventivoFormComponent } from './forms/mantenimiento-preventivo-form/mantenimiento-preventivo-form.component';
import { NgxSpinnerModule } from 'ngx-spinner';
import { CategoriasComponent } from './admin/categorias/categorias.component';
import { CategoriaFormComponent } from './forms/categoria-form/categoria-form.component';
import { AreaFormComponent } from './forms/area-form/area-form.component';
import { AreasComponent } from './admin/areas/areas.component';
import { CookieService } from 'ngx-cookie-service';
import { DataTablesModule } from 'angular-datatables';
import { ToastrModule } from 'ngx-toastr';
import { ProveedoresComponent } from './admin/proveedores/proveedores.component';
import { ProveedorFormComponent } from './forms/proveedor-form/proveedor-form.component';
import { LoginComponent } from './login/login.component';
import { RequisicionesComponent } from './admin/requisiciones/requisiciones.component';
import { RequisicionFormComponent } from './forms/requisicion-form/requisicion-form.component';
import { CalendarioComponent } from './admin/calendario/calendario.component';
import { CalendarModule, DateAdapter } from 'angular-calendar';
import { adapterFactory } from 'angular-calendar/date-adapters/date-fns';
import { NgbModalModule } from '@ng-bootstrap/ng-bootstrap';
import { registerLocaleData } from '@angular/common';
import localeEs from '@angular/common/locales/es';
import { GestionComponent } from './admin/gestion/gestion.component';
import { UsuariosComponent } from './admin/usuarios/usuarios.component';
registerLocaleData(localeEs);
import { NgxSelectModule } from 'ngx-select-ex';
import { BitacoraMedicionesComponent } from './admin/bitacora-mediciones/bitacora-mediciones.component';
import { BitacoraMedicionesFormComponent } from './forms/bitacora-mediciones-form/bitacora-mediciones-form.component';
import { AccordionModule } from 'ngx-accordion';
import { MantenimientoCorrectivoComponent } from './admin/mantenimiento-correctivo/mantenimiento-correctivo.component';
import { MantenimientoCorrectivoFormComponent } from './forms/mantenimiento-correctivo-form/mantenimiento-correctivo-form.component';
import { ActividadesComponent } from './admin/actividades/actividades.component';
import { PresupuestoComponent } from './admin/presupuesto/presupuesto.component';
import { ActividadesFormComponent } from './forms/actividades-form/actividades-form.component';
import { IncidenciasComponent } from './admin/incidencias/incidencias.component';
import { FinalizarMantCorFormComponent } from './forms/finalizar-mant-cor-form/finalizar-mant-cor-form.component';
import { HotelesComponent } from './admin/hoteles/hoteles.component';
import { HotelFormComponent } from './forms/hotel-form/hotel-form.component';
import { CalificarMantCorFormComponent } from './forms/calificar-mant-cor-form/calificar-mant-cor-form.component';


@NgModule({
  imports: [
    BrowserAnimationsModule,
    FormsModule,
    RouterModule,
    HttpClientModule,
    NavbarModule,
    FooterModule,
    SidebarModule,
    AppRoutingModule,
    ModalModule.forRoot(),
    CommonModule,
    NgxSpinnerModule,
    DataTablesModule,
    NgbModalModule,
    ToastrModule.forRoot(),
    CalendarModule.forRoot({
      provide: DateAdapter,
      useFactory: adapterFactory,
    }),
    AccordionModule,
    NgxSelectModule
  ],
  declarations: [
    AppComponent,
    AdminLayoutComponent,
    MantenimientoPreventivoComponent,
    MantenimientoPreventivoFormComponent,
    CategoriasComponent,
    CategoriaFormComponent,
    AreaFormComponent,
    AreasComponent,
    ProveedoresComponent,
    ProveedorFormComponent,
    LoginComponent,
    RequisicionesComponent,
    RequisicionFormComponent,
    CalendarioComponent,
    GestionComponent,
    UsuariosComponent,
    BitacoraMedicionesComponent,
    BitacoraMedicionesFormComponent,
    MantenimientoCorrectivoComponent,
    MantenimientoCorrectivoFormComponent,
    ActividadesComponent,
    PresupuestoComponent,
    ActividadesFormComponent,
    IncidenciasComponent,
    FinalizarMantCorFormComponent,
    HotelesComponent,
    HotelFormComponent,
    CalificarMantCorFormComponent
  ],
  providers: [CookieService, DatePipe],
  bootstrap: [AppComponent]
})
export class AppModule { }
