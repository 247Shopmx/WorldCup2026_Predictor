
import pandas as pd
import requests
import os
import sys

def send_telegram_message(message, token, chat_id):
    if not token or not chat_id:
        print('Error: TELEGRAM_BOT_TOKEN o TELEGRAM_CHAT_ID no configurados.')
        return
    
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print('✅ Notificación enviada a Telegram con éxito.')
        else:
            print(f'❌ Error de Telegram API: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'❌ Error de conexión: {e}')

def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    # Verificar si existe el archivo de predicciones en la ruta del runner
    pred_path = 'made_predictions/latest_predictions.csv'
    if not os.path.exists(pred_path):
        # Intentar ruta alternativa si el script corre desde carpetas internas
        pred_path = 'world_cup_2026/made_predictions/latest_predictions.csv'

    if not os.path.exists(pred_path):
        print(f'No hay predicciones para enviar en: {pred_path}')
        return

    df = pd.read_csv(pred_path)
    top_picks = df.head(5)

    message = "⚽ *Picks WC 2026 Automáticos* ⚽

"
    for _, row in top_picks.iterrows():
        message += f"⏰ {row['Datum']}
⚔ {row['Home']} vs {row['Away']}
📊 Probabilidad: Alta

"

    send_telegram_message(message, token, chat_id)

if __name__ == '__main__':
    main()
