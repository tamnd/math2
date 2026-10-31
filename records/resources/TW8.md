---
records:
    - id: TW8CNJEEWK
      kind: problem-set
      title: Kvant 1972, no. 12
      date: "1972"
      expressions:
        - key: e1
          kind: edition
          date: "1972"
          structure: TW8CNJEEWK/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1972-12
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: TW8PKZ0KHD
      kind: monograph
      title: 'Géométrie Algébrique Réelle et Formes Quadratiques: Journées S.M.F., Université de Rennes 1, Mai 1981'
      creators:
        - name: Jean-Louis Colliot-Thélène
          role: editor
        - name: Michel Coste
          role: editor
        - name: Louis Mahé
          role: editor
        - name: Marie-Françoise Roy
          role: editor
      date: "1982"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 11-06
          from: zbmath_search
        - code: 14-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: fr
          date: "1982"
          ids:
            doi: 10.1007/bfb0062247
            zbl: "0487.00005"
            zbl_id: "3765713"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783540119593"
                    - "9783540395485"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0062247
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3765713"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
