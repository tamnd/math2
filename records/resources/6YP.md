---
records:
    - id: 6YP7E22MWK
      kind: monograph
      title: One-Dimensional Ergodic Schrödinger Operators
      creators:
        - name: David Damanik
          role: author
        - name: Jake Fillman
          role: author
      date: "2022-08-18"
      msc:
        - code: 58-01
          from: zbmath_search
        - code: 35-01
          from: zbmath_search
        - code: 58J50
          from: zbmath_search
        - code: 58J51
          from: zbmath_search
        - code: 35J05
          from: zbmath_search
        - code: 35Q41
          from: zbmath_search
        - code: 81Q10
          from: zbmath_search
        - code: 37K10
          from: zbmath_search
        - code: 37B02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2022-08-18"
          ids:
            doi:
                - 10.1090/gsm/221
                - 10.1090/gsm/249
            zbl: "1504.58001"
            zbl_id: "7517379"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2022-08-18"
              ids:
                isbn:
                    - "9781470470852"
                    - "9781470456061"
                    - "9781470470869"
                    - "9781470472368"
              access:
                class: record
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "2025-01-15"
              ids:
                isbn:
                    - "9781470479251"
                    - "9781470465032"
                    - "9781470479244"
              access:
                class: record
      relations:
        - kind: part_of
          to: YBEDX3XNVA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/gsm/221
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/gsm/249
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "7517379"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 6YPMRQHMR5
      kind: preprint
      title: When Noise Estimation Hides Basis Misspecification in Repeated Bayesian Inverse Problems
      creators:
        - name: Rares Dimitrie Grozavescu
          role: author
        - name: Mark Girolami
          role: author
      date: "2026-09-29"
      msc:
        - code: 62-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: stat.ME
        - system: arxiv
          code: math.ST
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: stat.TH
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-29"
          ids:
            arxiv: "2609.37762"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.37762"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
---
