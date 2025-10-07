---

## 🧭 Objetivo del tutorial
- Configurar Git en ambas máquinas.
- Crear un repositorio en GitHub.
- Subir tu proyecto desde Windows.
- Clonarlo en Linux.
- Sincronizar cambios entre ambas.

---

## 🖥️ Parte 1: Configurar Git en tu máquina de oficina (Windows)

### 1. Instalar Git
- Descarga desde [git-scm.com](https://git-scm.com).
- Instálalo con las opciones por defecto.

### 2. Configurar tu identidad
Abre PowerShell o CMD:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

### 3. Crear tu proyecto
Abre VS Code y crea una carpeta con tu proyecto. Luego:

```bash
cd ruta/del/proyecto
git init
git add .
git commit -m "Primer commit desde oficina"
```

### 4. Crear un repositorio en GitHub
- Ve a [github.com](https://github.com) e inicia sesión.
- Haz clic en **New repository**.
- Ponle nombre (ej. `proyecto-sync`), deja público o privado.
- No marques "Initialize with README".

### 5. Conectar tu proyecto local con GitHub

```bash
git remote add origin https://github.com/tuusuario/proyecto-sync.git
git push -u origin master
```

> Si tu rama se llama `main`, cambia `master` por `main`.

---

## 🏠 Parte 2: Clonar el proyecto en tu máquina de casa (Linux)

### 1. Instalar Git
En terminal:

```bash
sudo apt update
sudo apt install git
```

### 2. Configurar tu identidad

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

### 3. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/proyecto-sync.git
cd proyecto-sync
```

Ya tienes el mismo proyecto en casa 🎉

---

## 🔁 Parte 3: Sincronizar cambios entre ambas máquinas

### Desde la oficina (Windows):

```bash
git add .
git commit -m "Cambios desde oficina"
git push
```

### Desde casa (Linux):

```bash
git pull
```

Y viceversa. Siempre que termines de trabajar en una máquina, haz `git push`, y en la otra, haz `git pull` antes de comenzar.

---

## 🧠 Extra: Consejos útiles

- Usa siempre el mismo nombre de rama (`main` o `master`).
- Puedes usar [SSH](https://docs.github.com/es/authentication/connecting-to-github-with-ssh) para evitar escribir tu contraseña cada vez.
- Si usas extensiones o configuraciones en VS Code, activa **Settings Sync** para mantenerlas iguales en ambas máquinas.
