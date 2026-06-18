
import pandas as pd
import requests
import os
import sys

def send_telegram_message(message, token, chat_id):
    url = f'https://api.github.com/bot{token}/sendMessage'
    # Corrección para la URL real de Telegram API (el usuario puso un formato similar a github)
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f'Error enviando Telegram: {e}')

def main():
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    if not os.path.exists('made_predictions/latest_predictions.csv'):
        print('No hay predicciones para enviar.')
        return

    df = pd.read_csv('made_predictions/latest_predictions.csv')
    
    # Simulación de filtro: Partidos con ranking muy dispar (Alta probabilidad)
    # En un escenario real, usaríamos las probabilidades calculadas por el modelo
    top_picks = df.sort_values(by=['home_league_position']).head(5)
    
    message = "⚽ *Nuevas Predicciones WC 2026* ⚽

"
    for _, row in top_picks.iterrows():
        message += f"⏰ {row['Datum']}
⚔ {row['Home']} vs {row['Away']}
📊 Pick sugerido: Victoria Local

"
    
    send_telegram_message(message, token, chat_id)
    print('Notificación enviada a Telegram.')

if __name__ == '__main__':
    main()
