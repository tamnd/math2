---
records:
    - id: VFZFC7Z7Z8
      kind: problem-set
      title: BMO Round 1 2024
      date: "2023-11-15"
      expressions:
        - key: e1
          kind: edition
          date: "2023-11-15"
          structure: VFZFC7Z7Z8/e1.json
      relations:
        - kind: part_of
          to: 8XFPR5H74Q
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: bmo
          snapshot: blake3:68eb2251465334659a3c67c12bc8e13877594a5a11510cf9a756eaf0f62db81c
          native_id: bmo1-2024
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: VFZTRNE6YW
      kind: monograph
      title: 'Probability Measures on Groups: Proceedings of the Fifth Conference Oberwolfach, Germany, January 29th – February 4, 1978'
      creators:
        - name: Herbert Heyer
          role: editor
      date: "1979"
      expressions:
        - key: e1
          kind: edition
          date: "1979"
          ids:
            doi:
                - 10.1007/bfb0063108
                - 10.1007/bfb0093215
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1979"
              ids:
                isbn:
                    - "9783540091240"
                    - "9783540354062"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783540115014"
                    - "9783540392064"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0063108
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0093215
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
