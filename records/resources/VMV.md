---
records:
    - id: VMV3J1E1T3
      kind: problem-set
      title: Kvant 1988, no. 2
      date: "1988"
      expressions:
        - key: e1
          kind: edition
          date: "1988"
          structure: VMV3J1E1T3/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1988-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: VMV9STVTV0
      kind: monograph
      title: Lectures on Probability Theory and Statistics
      creators:
        - name: Boris Tsirelson
          role: author
        - name: Wendelin Werner
          role: author
        - name: Jean Picard
          role: editor
      date: "2004"
      expressions:
        - key: e1
          kind: edition
          date: "2004"
          ids:
            doi: 10.1007/b96719
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2004"
              ids:
                isbn:
                    - "9783540213161"
                    - "9783540399827"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/b96719
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
