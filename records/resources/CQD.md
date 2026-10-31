---
records:
    - id: CQDJ3NZQVX
      kind: problem-set
      title: BMO 1985
      date: "1985-03-05"
      expressions:
        - key: e1
          kind: edition
          date: "1985-03-05"
      relations:
        - kind: part_of
          to: 8XFPR5H74Q
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: bmo
          snapshot: blake3:68eb2251465334659a3c67c12bc8e13877594a5a11510cf9a756eaf0f62db81c
          native_id: bmo-1985
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: CQDW7R3VWV
      kind: monograph
      title: Methods of Approximation Theory in Complex Analysis and Mathematical Physics
      creators:
        - name: Andrei A. Gonchar
          role: editor
        - name: Edward B. Saff
          role: editor
      date: "1993"
      msc:
        - code: 00B25
          from: zbmath_search
        - code: 30-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1993"
          ids:
            doi: 10.1007/bfb0117469
            zbl: "0779.00014"
            zbl_id: "467143"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1993"
              ids:
                isbn:
                    - "9783540569312"
                    - "9783540477921"
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
          native_id: 10.1007/bfb0117469
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "467143"
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
