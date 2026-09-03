import tkinter as tk
from tkinter import messagebox

# ==========================================
# IMPORT EXISTING TOOLS
# ==========================================

from tools.system_info import show_system_info
from tools.network_info import show_ip_info
from tools.ping_test import ping_host
from tools.port_checker import check_port
from tools.disk_space import show_disk_space
from tools.process_monitor import show_processes
from tools.file_organizer import organize_files
from tools.log_analyzer import analyze_log
from tools.password_checker import check_password


# ==========================================
# COLORS / STYLE
# ==========================================

BG_COLOR = "#0f172a"
SIDEBAR_COLOR = "#111827"
CARD_COLOR = "#1e293b"
BUTTON_COLOR = "#2563eb"
BUTTON_HOVER = "#1d4ed8"
TEXT_COLOR = "#f8fafc"
SECONDARY_TEXT = "#94a3b8"
SUCCESS_COLOR = "#22c55e"
DANGER_COLOR = "#ef4444"


# ==========================================
# MAIN APPLICATION
# ==========================================

class ITSupportToolkit(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("IT Support Toolkit")
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.configure(bg=BG_COLOR)

        self.create_ui()


    # ======================================
    # CREATE UI
    # ======================================

    def create_ui(self):

        # -------------------------------
        # SIDEBAR
        # -------------------------------

        self.sidebar = tk.Frame(
            self,
            bg=SIDEBAR_COLOR,
            width=240
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        # Logo / Title

        logo = tk.Label(
            self.sidebar,
            text="🛠 IT SUPPORT",
            bg=SIDEBAR_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI", 18, "bold")
        )

        logo.pack(
            pady=(30, 5)
        )

        subtitle = tk.Label(
            self.sidebar,
            text="Toolkit",
            bg=SIDEBAR_COLOR,
            fg=SECONDARY_TEXT,
            font=("Segoe UI", 10)
        )

        subtitle.pack(
            pady=(0, 25)
        )


        # -------------------------------
        # MENU BUTTONS
        # -------------------------------

        self.create_menu_button(
            "🖥  System Information",
            self.run_system_info
        )

        self.create_menu_button(
            "🌐  IP Information",
            self.run_ip_info
        )

        self.create_menu_button(
            "📡  Ping Test",
            self.run_ping
        )

        self.create_menu_button(
            "🔌  Port Checker",
            self.run_port
        )

        self.create_menu_button(
            "💾  Disk Space",
            self.run_disk
        )

        self.create_menu_button(
            "⚙  Running Processes",
            self.run_processes
        )

        self.create_menu_button(
            "📁  File Organizer",
            self.run_file_organizer
        )

        self.create_menu_button(
            "📄  Log Analyzer",
            self.run_log_analyzer
        )

        self.create_menu_button(
            "🔐  Password Checker",
            self.run_password_checker
        )


        # Exit button

        exit_button = tk.Button(
            self.sidebar,
            text="❌  Exit",
            command=self.exit_app,
            bg="#7f1d1d",
            fg=TEXT_COLOR,
            activebackground="#991b1b",
            activeforeground=TEXT_COLOR,
            relief="flat",
            borderwidth=0,
            font=("Segoe UI", 10, "bold"),
            anchor="w",
            padx=20,
            cursor="hand2"
        )

        exit_button.pack(
            side="bottom",
            fill="x",
            padx=15,
            pady=20,
            ipady=8
        )


        # -------------------------------
        # MAIN AREA
        # -------------------------------

        self.main_area = tk.Frame(
            self,
            bg=BG_COLOR
        )

        self.main_area.pack(
            side="right",
            fill="both",
            expand=True
        )


        # Header

        header = tk.Frame(
            self.main_area,
            bg=BG_COLOR
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 10)
        )

        self.page_title = tk.Label(
            header,
            text="Dashboard",
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI", 24, "bold")
        )

        self.page_title.pack(
            anchor="w"
        )

        self.page_description = tk.Label(
            header,
            text="IT Support and System Administration Toolkit",
            bg=BG_COLOR,
            fg=SECONDARY_TEXT,
            font=("Segoe UI", 11)
        )

        self.page_description.pack(
            anchor="w",
            pady=(5, 0)
        )


        # Content area

        self.content = tk.Frame(
            self.main_area,
            bg=BG_COLOR
        )

        self.content.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )


        self.show_dashboard()


    # ======================================
    # MENU BUTTON
    # ======================================

    def create_menu_button(self, text, command):

        button = tk.Button(
            self.sidebar,
            text=text,
            command=command,
            bg=SIDEBAR_COLOR,
            fg=SECONDARY_TEXT,
            activebackground=BUTTON_COLOR,
            activeforeground=TEXT_COLOR,
            relief="flat",
            borderwidth=0,
            font=("Segoe UI", 10),
            anchor="w",
            padx=20,
            cursor="hand2"
        )

        button.pack(
            fill="x",
            padx=15,
            pady=3,
            ipady=8
        )

        # Hover effect

        button.bind(
            "<Enter>",
            lambda event: button.configure(
                bg=BUTTON_COLOR,
                fg=TEXT_COLOR
            )
        )

        button.bind(
            "<Leave>",
            lambda event: button.configure(
                bg=SIDEBAR_COLOR,
                fg=SECONDARY_TEXT
            )
        )


    # ======================================
    # CLEAR CONTENT
    # ======================================

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()


    # ======================================
    # DASHBOARD
    # ======================================

    def show_dashboard(self):

        self.page_title.config(
            text="Dashboard"
        )

        self.page_description.config(
            text="Welcome to your IT Support Toolkit"
        )

        self.clear_content()


        # Dashboard title

        welcome = tk.Label(
            self.content,
            text="IT Support Toolkit",
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI", 20, "bold")
        )

        welcome.pack(
            anchor="w",
            pady=(10, 20)
        )


        # Cards container

        cards = tk.Frame(
            self.content,
            bg=BG_COLOR
        )

        cards.pack(
            fill="x"
        )


        self.create_card(
            cards,
            "🖥",
            "System Information",
            "View operating system and computer information",
            self.run_system_info
        )

        self.create_card(
            cards,
            "🌐",
            "Network",
            "View IP and network information",
            self.run_ip_info
        )

        self.create_card(
            cards,
            "💾",
            "Disk Space",
            "Check available disk storage",
            self.run_disk
        )

        self.create_card(
            cards,
            "⚙",
            "Processes",
            "View currently running processes",
            self.run_processes
        )


        # Information box

        info = tk.Frame(
            self.content,
            bg=CARD_COLOR
        )

        info.pack(
            fill="both",
            expand=True,
            pady=30
        )


        tk.Label(
            info,
            text="Available Tools",
            bg=CARD_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )


        tools_text = """
• System Information
• IP Information
• Ping Test
• TCP Port Checker
• Disk Space Monitor
• Running Process Monitor
• File Organizer
• Log Analyzer
• Password Strength Checker
        """

        tk.Label(
            info,
            text=tools_text,
            justify="left",
            bg=CARD_COLOR,
            fg=SECONDARY_TEXT,
            font=("Segoe UI", 11),
            anchor="w"
        ).pack(
            anchor="w",
            padx=25
        )


    # ======================================
    # DASHBOARD CARD
    # ======================================

    def create_card(
        self,
        parent,
        icon,
        title,
        description,
        command
    ):

        card = tk.Frame(
            parent,
            bg=CARD_COLOR,
            width=210,
            height=150
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=7
        )

        card.pack_propagate(False)


        tk.Label(
            card,
            text=icon,
            bg=CARD_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI Emoji", 25)
        ).pack(
            pady=(15, 5)
        )


        tk.Label(
            card,
            text=title,
            bg=CARD_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI", 12, "bold")
        ).pack()


        tk.Label(
            card,
            text=description,
            bg=CARD_COLOR,
            fg=SECONDARY_TEXT,
            font=("Segoe UI", 9),
            wraplength=180
        ).pack(
            pady=5
        )


        card.bind(
            "<Button-1>",
            lambda event: command()
        )


    # ======================================
    # DISPLAY TOOL RESULT
    # ======================================

    def show_result(self, title, result):

        self.clear_content()

        self.page_title.config(
            text=title
        )

        self.page_description.config(
            text="Tool Result"
        )


        result_frame = tk.Frame(
            self.content,
            bg=CARD_COLOR
        )

        result_frame.pack(
            fill="both",
            expand=True
        )


        # Result header

        tk.Label(
            result_frame,
            text=title,
            bg=CARD_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=25,
            pady=(25, 10)
        )


        # Text area

        text = tk.Text(
            result_frame,
            bg="#0b1120",
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            font=("Consolas", 10),
            relief="flat",
            padx=15,
            pady=15,
            wrap="word"
        )

        text.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(5, 25)
        )


        text.insert(
            "1.0",
            str(result)
        )

        text.config(
            state="disabled"
        )


    # ======================================
    # RUN TOOLS
    # ======================================

    def run_system_info(self):

        try:
            result = show_system_info()

            self.show_result(
                "System Information",
                result
            )

        except Exception as error:

            self.show_error(error)


    def run_ip_info(self):

        try:
            result = show_ip_info()

            self.show_result(
                "IP Information",
                result
            )

        except Exception as error:

            self.show_error(error)


    def run_ping(self):

        self.input_window(
            "Ping Test",
            "Enter hostname or IP address:",
            ping_host
        )


    def run_port(self):

        self.input_window(
            "Port Checker",
            "Enter host and port (example: google.com 443):",
            check_port
        )


    def run_disk(self):

        try:

            result = show_disk_space()

            self.show_result(
                "Disk Space",
                result
            )

        except Exception as error:

            self.show_error(error)


    def run_processes(self):

        try:

            result = show_processes()

            self.show_result(
                "Running Processes",
                result
            )

        except Exception as error:

            self.show_error(error)


    def run_file_organizer(self):

        self.input_window(
            "File Organizer",
            "Enter folder path to organize:",
            organize_files
        )


    def run_log_analyzer(self):

        self.input_window(
            "Log Analyzer",
            "Enter log file path [default: logs/server.log]:",
            analyze_log
        )


    def run_password_checker(self):

        self.input_window(
            "Password Checker",
            "Enter password:",
            check_password,
            password=True
        )


    # ======================================
    # INPUT WINDOW
    # ======================================

    def input_window(
        self,
        title,
        label_text,
        function,
        password=False
    ):

        window = tk.Toplevel(self)

        window.title(title)
        window.geometry("450x220")
        window.configure(bg=BG_COLOR)

        window.transient(self)
        window.grab_set()


        tk.Label(
            window,
            text=title,
            bg=BG_COLOR,
            fg=TEXT_COLOR,
            font=("Segoe UI", 18, "bold")
        ).pack(
            pady=(25, 15)
        )


        tk.Label(
            window,
            text=label_text,
            bg=BG_COLOR,
            fg=SECONDARY_TEXT,
            font=("Segoe UI", 10)
        ).pack()


        entry = tk.Entry(
            window,
            bg="#1e293b",
            fg=TEXT_COLOR,
            insertbackground=TEXT_COLOR,
            relief="flat",
            font=("Segoe UI", 11),
            show="*" if password else ""
        )

        entry.pack(
            fill="x",
            padx=40,
            pady=15,
            ipady=8
        )

        entry.focus()


        def execute():

            value = entry.get().strip()

            if not value and function != analyze_log:

                messagebox.showwarning(
                    "Input Required",
                    "Please enter a value."
                )

                return

            try:

                # --------------------------------
                # Port checker
                # --------------------------------

                if function == check_port:

                    parts = value.split()

                    if len(parts) != 2:

                        messagebox.showerror(
                            "Invalid Input",
                            "Use this format:\n\nhost port\n\nExample:\ngoogle.com 443"
                        )

                        return

                    result = function(
                        parts[0],
                        int(parts[1])
                    )

                else:

                    result = function(value)


                window.destroy()

                self.show_result(
                    title,
                    result
                )


            except Exception as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )


        tk.Button(
            window,
            text="Run Tool",
            command=execute,
            bg=BUTTON_COLOR,
            fg=TEXT_COLOR,
            activebackground=BUTTON_HOVER,
            activeforeground=TEXT_COLOR,
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2",
            padx=30,
            pady=8
        ).pack()


        entry.bind(
            "<Return>",
            lambda event: execute()
        )


    # ======================================
    # ERROR
    # ======================================

    def show_error(self, error):

        messagebox.showerror(
            "Tool Error",
            f"An error occurred:\n\n{error}"
        )


    # ======================================
    # EXIT
    # ======================================

    def exit_app(self):

        answer = messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        )

        if answer:
            self.destroy()


# ==========================================
# APPLICATION START
# ==========================================

if __name__ == "__main__":

    app = ITSupportToolkit()

    app.mainloop()