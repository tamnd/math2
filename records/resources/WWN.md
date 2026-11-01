---
records:
    - id: WWNKPFHYBT
      kind: problem-set
      title: IMO 1983
      creators:
        - name: IMO Problem Selection Committee
          role: author
      date: "1983"
      msc:
        - code: 00A07
          from: imo
        - code: 97U40
          from: imo
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1983"
      relations:
        - kind: part_of
          to: 931689K6X2
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: imo
          snapshot: blake3:c564548c1a7c5bfe4e71cf81d61c599a9d4016d698feff8fb0bc9beb0e2f88f9
          native_id: "1983"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: WWNPHX4QEF
      kind: monograph
      title: An Introduction to Probabilistic Modeling
      creators:
        - name: Pierre Brémaud
          role: author
      date: "1988"
      msc:
        - code: 60-01
          from: zbmath_search
        - code: 60Kxx
          from: zbmath_search
        - code: 60Fxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1988"
          ids:
            doi: 10.1007/978-1-4612-1046-7
            zbl: "0652.60002"
            zbl_id: "193599"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1988"
              ids:
                isbn:
                    - "9780387964607"
                    - "9781461210467"
              access:
                class: record
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-1046-7
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "193599"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
