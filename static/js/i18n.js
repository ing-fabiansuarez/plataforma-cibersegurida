// Sistema de Internacionalización
class I18nManager {
    constructor() {
        this.currentLanguage = localStorage.getItem('cyberlearn-language') || 'es';
        this.translations = {
            es: {
                // Navegación principal
                'Academia Gamificada de Ciberseguridad': 'Academia Gamificada de Ciberseguridad',
                'Ingresar': 'Ingresar',
                'Mi Perfil': 'Mi Perfil',
                'Hola': 'Hola',
                'Salir': 'Salir',
                'Registrarse': 'Registrarse',
                'Cambiar tema': 'Cambiar tema',
                
                // Login y Registro
                'Inicia Sesión': 'Inicia Sesión',
                'Terminal de Acceso Seguro v2.4': 'Terminal de Acceso Seguro v2.4',
                'Error de Autenticación': 'Error de Autenticación',
                'Usuario': 'Usuario',
                'nombre_de_usuario': 'nombre_de_usuario',
                'Contraseña': 'Contraseña',
                '¿Olvidaste tu clave?': '¿Olvidaste tu clave?',
                'ACCEDER AL SISTEMA': 'ACCEDER AL SISTEMA',
                '¿No tienes acceso?': '¿No tienes acceso?',
                'Crea una cuenta': 'Crea una cuenta',
                'NODO DE SEGURIDAD ACTIVADO': 'NODO DE SEGURIDAD ACTIVADO',
                'Crear Cuenta': 'Crear Cuenta',
                'Únete a la Academia': 'Únete a la Academia',
                'Crea tu terminal de estudiante y empieza a hackear': 'Crea tu terminal de estudiante y empieza a hackear',
                'Error en el Registro': 'Error en el Registro',
                'REGISTRARSE COMO ESTUDIANTE': 'REGISTRARSE COMO ESTUDIANTE',
                '¿Ya tienes una cuenta operativa?': '¿Ya tienes una cuenta operativa?',
                
                // Anuncios
                'Anuncios': 'Anuncios',
                'Comunicados del sector de ciberseguridad': 'Comunicados del sector de ciberseguridad',
                'EN LÍNEA': 'EN LÍNEA',
                'Nuevo comunicado': 'Nuevo comunicado',
                'Avatar': 'Avatar',
                'Reacciones': 'Reacciones',
                'Comentarios': 'Comentarios',
                'Lecturas': 'Lecturas',
                'Publicado por': 'Publicado por',
                'Me gusta': 'Me gusta',
                'Leído': 'Leído',
                'Marcar como leído': 'Marcar como leído',
                'Escribe un comentario...': 'Escribe un comentario...',
                'ahora': 'ahora',
                'No hay anuncios aún': 'No hay anuncios aún',
                'Los comunicados aparecerán aquí cuando un instructor los publique.': 'Los comunicados aparecerán aquí cuando un instructor los publique.',
                
                // Panel de Instructor
                'Panel de Instructor': 'Panel de Instructor',
                'Arquitectura y despliegue de desafíos tácticos de ciberseguridad.': 'Arquitectura y despliegue de desafíos tácticos de ciberseguridad.',
                'Nuevo Desafío': 'Nuevo Desafío',
                'Total Retos': 'Total Retos',
                'Publicados': 'Publicados',
                'Soluciones Totales': 'Soluciones Totales',
                'Editar': 'Editar',
                'Eliminar': 'Eliminar',
                'Solo lectura': 'Solo lectura',
                'Dificultad': 'Dificultad',
                'Puntos': 'Puntos',
                'Publicado,Borrador': 'Publicado,Borrador',
                'soluciones': 'soluciones',
                'Zona de Operaciones Vacía': 'Zona de Operaciones Vacía',
                'No se han detectado desafíos en tu sector. Inicia el despliegue de tu primer reto táctico.': 'No se han detectado desafíos en tu sector. Inicia el despliegue de tu primer reto táctico.',
                'Crear Primer Reto': 'Crear Primer Reto',
                
                // Tabs Navigation
                '¿Qué es?': 'What is it?',
                'Eventos': 'Events',
                'Foro': 'Forum',
                'Estudiantes': 'Students',
                'Retos': 'Challenges',
                'Insignias': 'Badges',
                'Encuestas': 'Surveys',
                'Documentos': 'Documents',
                'Repositorio': 'Repository',
                'Nuestro Himno': 'Our Anthem',
                'Ir a Dropbox': 'Go to Dropbox',
                'Admin': 'Admin',
                
                // Página principal
                'Semillero CHATS': 'Semillero CHATS',
                'Semillero de Seguridad Informática': 'Semillero de Seguridad Informática',
                'Ingeniería de Sistemas — Ciberseguridad, Hacking Ético, Análisis Forense, Tecnologías de la Información y SGSI.': 'Ingeniería de Sistemas — Ciberseguridad, Hacking Ético, Análisis Forense, Tecnologías de la Información y SGSI.',
                'Unirse ahora': 'Unirse ahora',
                'Anuncios': 'Anuncios',
                'Investigación Destacada': 'Investigación Destacada',
                'Análisis del Vector de Ataque: Cryptojacking': 'Análisis del Vector de Ataque: Cryptojacking',
                'Los entornos digitales orientados a la Web han aportado un gran número de beneficios, sin embargo, han traído consigo múltiples amenazas como el llamado Cryptojacking.': 'Los entornos digitales orientados a la Web han aportado un gran número de beneficios, sin embargo, han traído consigo múltiples amenazas como el llamado Cryptojacking.',
                'Generar políticas para minimizar la interacción en sitios web maliciosos.': 'Generar políticas para minimizar la interacción en sitios web maliciosos.',
                'Estrategias de sensibilización mediante escenarios de prueba reales.': 'Estrategias de sensibilización mediante escenarios de prueba reales.',
                'Capacitaciones periódicas con evaluaciones sobre las temáticas tratadas.': 'Capacitaciones periódicas con evaluaciones sobre las temáticas tratadas.',
                'Auditorías periódicas y acciones correctivas según las oportunidades de mejora.': 'Auditorías periódicas y acciones correctivas según las oportunidades de mejora.',
                'Nuestros Proyectos': 'Nuestros Proyectos',
                'Adopción de Estrategia Zero Trust': 'Adopción de Estrategia Zero Trust',
                'Análisis descriptivo del enfoque arquitectónico de Zero Trust para impulsar su adopción como estrategia de ciberseguridad en organizaciones públicas y privadas.': 'Análisis descriptivo del enfoque arquitectónico de Zero Trust para impulsar su adopción como estrategia de ciberseguridad en organizaciones públicas y privadas.',
                'Gestión de Actas con Firma Electrónica': 'Gestión de Actas con Firma Electrónica',
                'Plataforma para la gestión de actas de reunión usando firma electrónica para garantizar integridad y autenticidad.': 'Plataforma para la gestión de actas de reunión usando firma electrónica para garantizar integridad y autenticidad.',
                'Análisis Malware Cryptojacking': 'Análisis Malware Cryptojacking',
                'Estudio descriptivo del vector de ataque del malware Cryptojacking en plataformas web y su impacto en el rendimiento.': 'Estudio descriptivo del vector de ataque del malware Cryptojacking en plataformas web y su impacto en el rendimiento.',
                'Gamificación en Informática Forense': 'Gamificación en Informática Forense',
                'Videojuego para el aprendizaje de la fundamentación conceptual en Informática forense de manera interactiva.': 'Videojuego para el aprendizaje de la fundamentación conceptual en Informática forense de manera interactiva.',
                'Nuestros Integrantes': 'Nuestros Integrantes',
                'Estudiantes Activos en el semillero': 'Estudiantes Activos en el semillero',
                'Ing. Sistemas': 'Ing. Sistemas',
                'Score': 'Puntuación',
                'Excelente desempeño en retos': 'Excelente desempeño en retos',
                'Gran participación en el foro': 'Gran participación en el foro',
                '"Análisis descriptivo del vector de ataque del malware cryptojacking en plataformas web. Una experiencia enriquecedora en el semillero desde 2019."': '"Análisis descriptivo del vector de ataque del malware cryptojacking en plataformas web. Una experiencia enriquecedora en el semillero desde 2019."',
                'Estudiante 9 semestre / Ingeniería de Sistemas': 'Estudiante 9 semestre / Ingeniería de Sistemas',
                'Emergencias': 'Emergencias',
                'Registros activos': 'Registros activos',
                'Eventos': 'Eventos',
                'En bitácora': 'En bitácora',
                'Observaciones': 'Observaciones',
                'Registradas': 'Registradas',
                'Último usuario': 'Último usuario',
                'Sin actividad': 'Sin actividad'
            },
            en: {
                // Navegación principal
                'Academia Gamificada de Ciberseguridad': 'Gamified Cybersecurity Academy',
                'Ingresar': 'Login',
                'Mi Perfil': 'My Profile',
                'Hola': 'Hello',
                'Salir': 'Logout',
                'Registrarse': 'Sign Up',
                'Cambiar tema': 'Toggle theme',
                
                // Login y Registro
                'Inicia Sesión': 'Sign In',
                'Terminal de Acceso Seguro v2.4': 'Secure Access Terminal v2.4',
                'Error de Autenticación': 'Authentication Error',
                'Usuario': 'Username',
                'nombre_de_usuario': 'username',
                'Contraseña': 'Password',
                '¿Olvidaste tu clave?': 'Forgot your password?',
                'ACCEDER AL SISTEMA': 'ACCESS SYSTEM',
                '¿No tienes acceso?': 'Don\'t have access?',
                'Crea una cuenta': 'Create an account',
                'NODO DE SEGURIDAD ACTIVADO': 'SECURITY NODE ACTIVATED',
                'Crear Cuenta': 'Create Account',
                'Únete a la Academia': 'Join the Academy',
                'Crea tu terminal de estudiante y empieza a hackear': 'Create your student terminal and start hacking',
                'Error en el Registro': 'Registration Error',
                'REGISTRARSE COMO ESTUDIANTE': 'REGISTER AS STUDENT',
                '¿Ya tienes una cuenta operativa?': 'Already have an account?',
                
                // Anuncios
                'Anuncios': 'Announcements',
                'Comunicados del sector de ciberseguridad': 'Cybersecurity sector communications',
                'EN LÍNEA': 'ONLINE',
                'Nuevo comunicado': 'New announcement',
                'Avatar': 'Avatar',
                'Reacciones': 'Reactions',
                'Comentarios': 'Comments',
                'Lecturas': 'Reads',
                'Publicado por': 'Published by',
                'Me gusta': 'Like',
                'Leído': 'Read',
                'Marcar como leído': 'Mark as read',
                'Escribe un comentario...': 'Write a comment...',
                'ahora': 'now',
                'No hay anuncios aún': 'No announcements yet',
                'Los comunicados aparecerán aquí cuando un instructor los publique.': 'Announcements will appear here when an instructor publishes them.',
                
                // Panel de Instructor
                'Panel de Instructor': 'Instructor Dashboard',
                'Arquitectura y despliegue de desafíos tácticos de ciberseguridad.': 'Architecture and deployment of tactical cybersecurity challenges.',
                'Nuevo Desafío': 'New Challenge',
                'Total Retos': 'Total Challenges',
                'Publicados': 'Published',
                'Soluciones Totales': 'Total Solutions',
                'Editar': 'Edit',
                'Eliminar': 'Delete',
                'Solo lectura': 'Read only',
                'Dificultad': 'Difficulty',
                'Puntos': 'Points',
                'Publicado,Borrador': 'Published,Draft',
                'soluciones': 'solves',
                'Zona de Operaciones Vacía': 'Empty Operations Zone',
                'No se han detectado desafíos en tu sector. Inicia el despliegue de tu primer reto táctico.': 'No challenges detected in your sector. Start deploying your first tactical challenge.',
                'Crear Primer Reto': 'Create First Challenge',
                
                // Tabs Navigation
                '¿Qué es?': 'What is it?',
                'Eventos': 'Events',
                'Foro': 'Forum',
                'Estudiantes': 'Students',
                'Retos': 'Challenges',
                'Insignias': 'Badges',
                'Encuestas': 'Surveys',
                'Documentos': 'Documents',
                'Repositorio': 'Repository',
                'Nuestro Himno': 'Our Anthem',
                'Ir a Dropbox': 'Go to Dropbox',
                'Admin': 'Admin',
                
                // Página principal
                'Semillero CHATS': 'CHATS Seedbed',
                'Semillero de Seguridad Informática': 'Computer Security Seedbed',
                'Ingeniería de Sistemas — Ciberseguridad, Hacking Ético, Análisis Forense, Tecnologías de la Información y SGSI.': 'Systems Engineering — Cybersecurity, Ethical Hacking, Forensic Analysis, Information Technologies and ISMS.',
                'Unirse ahora': 'Join Now',
                'Anuncios': 'Announcements',
                'Investigación Destacada': 'Featured Research',
                'Análisis del Vector de Ataque: Cryptojacking': 'Attack Vector Analysis: Cryptojacking',
                'Los entornos digitales orientados a la Web han aportado un gran número de beneficios, sin embargo, han traído consigo múltiples amenazas como el llamado Cryptojacking.': 'Web-oriented digital environments have brought many benefits, however, they have also brought multiple threats such as so-called Cryptojacking.',
                'Generar políticas para minimizar la interacción en sitios web maliciosos.': 'Generate policies to minimize interaction with malicious websites.',
                'Estrategias de sensibilización mediante escenarios de prueba reales.': 'Awareness strategies through real test scenarios.',
                'Capacitaciones periódicas con evaluaciones sobre las temáticas tratadas.': 'Periodic training with evaluations on the topics covered.',
                'Auditorías periódicas y acciones correctivas según las oportunidades de mejora.': 'Periodic audits and corrective actions according to improvement opportunities.',
                'Nuestros Proyectos': 'Our Projects',
                'Adopción de Estrategia Zero Trust': 'Zero Trust Strategy Adoption',
                'Análisis descriptivo del enfoque arquitectónico de Zero Trust para impulsar su adopción como estrategia de ciberseguridad en organizaciones públicas y privadas.': 'Descriptive analysis of the Zero Trust architectural approach to drive its adoption as a cybersecurity strategy in public and private organizations.',
                'Gestión de Actas con Firma Electrónica': 'Minutes Management with Electronic Signature',
                'Plataforma para la gestión de actas de reunión usando firma electrónica para garantizar integridad y autenticidad.': 'Platform for meeting minutes management using electronic signature to guarantee integrity and authenticity.',
                'Análisis Malware Cryptojacking': 'Cryptojacking Malware Analysis',
                'Estudio descriptivo del vector de ataque del malware Cryptojacking en plataformas web y su impacto en el rendimiento.': 'Descriptive study of the Cryptojacking malware attack vector on web platforms and its impact on performance.',
                'Gamificación en Informática Forense': 'Gamification in Computer Forensics',
                'Videojuego para el aprendizaje de la fundamentación conceptual en Informática forense de manera interactiva.': 'Video game for learning conceptual foundations in Computer Forensics interactively.',
                'Nuestros Integrantes': 'Our Members',
                'Estudiantes Activos en el semillero': 'Active Students in the seedbed',
                'Ing. Sistemas': 'Systems Eng.',
                'Score': 'Score',
                'Excelente desempeño en retos': 'Excellent performance in challenges',
                'Gran participación en el foro': 'Great participation in the forum',
                '"Análisis descriptivo del vector de ataque del malware cryptojacking en plataformas web. Una experiencia enriquecedora en el semillero desde 2019."': '"Descriptive analysis of the cryptojacking malware attack vector on web platforms. An enriching experience in the seedbed since 2019."',
                'Estudiante 9 semestre / Ingeniería de Sistemas': '9th semester Student / Systems Engineering',
                'Emergencias': 'Emergencies',
                'Registros activos': 'Active records',
                'Eventos': 'Events',
                'En bitácora': 'In log',
                'Observaciones': 'Observations',
                'Registradas': 'Registered',
                'Último usuario': 'Last user',
                'Sin actividad': 'No activity'
            }
        };
        
        this.init();
    }
    
    init() {
        this.updateLanguageSelector();
        this.translatePage();
        this.setupEventListeners();
    }
    
    setupEventListeners() {
        // Escuchar cambios en el selector de idioma
        const languageSelector = document.getElementById('language-selector');
        if (languageSelector) {
            languageSelector.addEventListener('change', (e) => {
                this.changeLanguage(e.target.value);
            });
        }
        
        // También escuchar formularios de idioma de Django
        const languageForms = document.querySelectorAll('form[action*="set_language"]');
        languageForms.forEach(form => {
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                const select = form.querySelector('select[name="language"]');
                if (select) {
                    this.changeLanguage(select.value);
                }
            });
        });
    }
    
    changeLanguage(lang) {
        this.currentLanguage = lang;
        localStorage.setItem('cyberlearn-language', lang);
        this.updateLanguageSelector();
        this.translatePage();
        
        // Actualizar el atributo lang del HTML
        document.documentElement.lang = lang;
    }
    
    updateLanguageSelector() {
        // Actualizar selectores de idioma
        const selectors = document.querySelectorAll('#language-selector, select[name="language"]');
        selectors.forEach(selector => {
            if (selector) {
                selector.value = this.currentLanguage;
            }
        });
    }
    
    translatePage() {
        // Traducir todos los elementos con data-translate
        const elements = document.querySelectorAll('[data-translate]');
        elements.forEach(element => {
            const key = element.getAttribute('data-translate');
            const translation = this.translate(key);
            if (translation && element.textContent !== translation) {
                element.textContent = translation;
            }
        });
        
        // Traducir elementos con data-translate-html
        const htmlElements = document.querySelectorAll('[data-translate-html]');
        htmlElements.forEach(element => {
            const key = element.getAttribute('data-translate-html');
            const translation = this.translate(key);
            if (translation && element.innerHTML !== translation) {
                element.innerHTML = translation;
            }
        });
        
        // Traducir elementos con data-translate-title
        const titleElements = document.querySelectorAll('[data-translate-title]');
        titleElements.forEach(element => {
            const key = element.getAttribute('data-translate-title');
            const translation = this.translate(key);
            if (translation) {
                element.setAttribute('title', translation);
            }
        });
        
        // Traducir placeholder
        const placeholderElements = document.querySelectorAll('[data-translate-placeholder]');
        placeholderElements.forEach(element => {
            const key = element.getAttribute('data-translate-placeholder');
            const translation = this.translate(key);
            if (translation) {
                element.setAttribute('placeholder', translation);
            }
        });
    }
    
    translate(key) {
        return this.translations[this.currentLanguage][key] || key;
    }
    
    // Función para agregar nuevas traducciones dinámicamente
    addTranslations(language, newTranslations) {
        if (!this.translations[language]) {
            this.translations[language] = {};
        }
        Object.assign(this.translations[language], newTranslations);
        this.translatePage();
    }
}

// Inicializar el sistema cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', function() {
    window.i18n = new I18nManager();
});
